#!/usr/bin/env python3
"""Mantenimiento de los apuntes. Ejecútalo desde la raíz del repositorio (Python 3.8 o superior).

  python3 herramientas/mantenimiento.py actualizar
      Regenera los bloques automáticos (pies, índices, categorías, mapa, cerebro y grafo) y valida.
      Es el comando que hay que ejecutar después de cualquier cambio.

  python3 herramientas/mantenimiento.py nueva-area SLUG "Nombre" ORDEN
  python3 herramientas/mantenimiento.py nueva-leccion AREA ORDEN SLUG "Título"
  python3 herramientas/mantenimiento.py nueva-categoria RUTA "Nombre" ORDEN
  python3 herramientas/mantenimiento.py nuevo-concepto SLUG "Título" "alias1|alias2" CATEGORIA
      Crean archivos con su estructura. Cada uno trae una línea PENDIENTE: que hay que reemplazar.

  python3 herramientas/mantenimiento.py regenerar | validar
      Pasos sueltos de "actualizar".

Los bloques entre <!-- auto:nombre --> y <!-- /auto:nombre --> se generan solos. No los edites.
Los enlaces entre conceptos se escriben a mano. El script no los inserta automáticamente.
"""
import json
import posixpath
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parent.parent
RAIZ_MAYUSCULAS = {"README.md", "MAPA.md", "MANTENIMIENTO.md"}
CARPETAS_ESPECIALES = {"conceptos", "cerebro", "herramientas"}
PENDIENTE = "PENDIENTE:"
SLUG_RE = re.compile(r"[a-z0-9]+(-[a-z0-9]+)*")

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
BLOQUE_AUTO_RE = re.compile(r"\n*<!-- auto:(\w+) -->.*?<!-- /auto:\1 -->\n*", re.S)
ENLACE_RE = re.compile(r"(!?)\[([^\]\n]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")
PROT_RE = re.compile(r"(`[^`\n]*`|!?\[[^\]\n]*\]\([^)\n]*\)|<[^>\n]+>)")
MIN_PALABRAS_CONCEPTO = 120


# ------------------------------------------------------------------ lectura y formato

def leer_frontmatter(texto):
    """Devuelve (datos, cuerpo). Soporta valores simples y listas [a, b]."""
    m = FM_RE.match(texto)
    if not m:
        return {}, texto
    datos = {}
    for linea in m.group(1).splitlines():
        if ":" not in linea:
            continue
        clave, valor = linea.split(":", 1)
        valor = valor.strip()
        if valor.startswith("["):
            datos[clave.strip()] = [v.strip().strip('"') for v in valor.strip("[]").split(",") if v.strip()]
        else:
            datos[clave.strip()] = valor.strip('"')
    return datos, texto[m.end():]


def fm_texto(datos):
    lineas = ["---"]
    for k, v in datos.items():
        if isinstance(v, list):
            lineas.append(f"{k}: [" + ", ".join(f'"{x}"' for x in v) + "]")
        elif isinstance(v, int):
            lineas.append(f"{k}: {v}")
        else:
            lineas.append(f'{k}: "{v}"')
    lineas.append("---")
    return "\n".join(lineas) + "\n\n"


def documentos(raiz):
    """Rutas (posix) de todos los .md del repositorio, sin herramientas ni archivos ocultos."""
    salida = []
    for p in sorted(raiz.rglob("*.md")):
        rel = p.relative_to(raiz).as_posix()
        if rel.startswith(("herramientas/", ".")) or "/." in rel:
            continue
        salida.append(rel)
    return salida


def areas(raiz):
    """Áreas de lecciones = carpetas con indice.md que declara 'area' y 'area_orden'."""
    encontradas = {}
    for idx in raiz.glob("*/indice.md"):
        fm, _ = leer_frontmatter(idx.read_text(encoding="utf-8"))
        if "area" in fm and "area_orden" in fm:
            encontradas[fm["area"]] = {
                "nombre": fm.get("nombre", fm["area"]),
                "orden": int(fm["area_orden"]),
                "indice": f"{fm['area']}/indice.md",
            }
    return dict(sorted(encontradas.items(), key=lambda kv: kv[1]["orden"]))


def categorias(raiz):
    """Categorías de conceptos = carpetas de conceptos/ con categoria.md.
    Devuelve {ruta: datos} con la ruta relativa a conceptos/ (por ejemplo 'bases-de-datos/modelado')."""
    encontradas = {}
    for p in sorted((raiz / "conceptos").rglob("categoria.md")):
        fm, _ = leer_frontmatter(p.read_text(encoding="utf-8"))
        ruta = p.parent.relative_to(raiz / "conceptos").as_posix()
        encontradas[ruta] = {
            "nombre": fm.get("nombre", ruta),
            "orden": int(fm.get("orden", 99)),
            "indice": p.relative_to(raiz).as_posix(),
            "padre": posixpath.dirname(ruta) or None,
        }
    return encontradas


def hijas(cats, padre):
    """Categorías hijas de una categoría (o de la raíz si padre es None), en orden."""
    return sorted(
        (r for r, d in cats.items() if d["padre"] == padre),
        key=lambda r: (cats[r]["orden"], r),
    )


def nombre_categoria(cats, ruta):
    """Ruta completa con nombres, por ejemplo 'Bases de datos › Modelado'."""
    partes, actual = [], ruta
    while actual:
        partes.append(cats[actual]["nombre"])
        actual = cats[actual]["padre"]
    return " › ".join(reversed(partes))


def prosa(texto):
    """Cuerpo sin frontmatter ni bloques automáticos."""
    _, cuerpo = leer_frontmatter(texto)
    return BLOQUE_AUTO_RE.sub("\n", cuerpo)


def sin_bloques(texto):
    """Cuerpo sin frontmatter ni bloques de código delimitados."""
    _, cuerpo = leer_frontmatter(texto)
    return re.sub(r"```.*?```", "", cuerpo, flags=re.S)


def sin_codigo(texto):
    """Como sin_bloques, y además sin código en línea."""
    return re.sub(r"`[^`\n]*`", "", sin_bloques(texto))


def cuerpo_visible(texto):
    """Solo prosa, sin código, comentarios ni destinos de enlaces. Se usa para contar menciones."""
    cuerpo = re.sub(r"<!--.*?-->", "", prosa(texto), flags=re.S)
    cuerpo = re.sub(r"```.*?```", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"`[^`\n]*`", "", cuerpo)
    return re.sub(r"\]\([^)\n]*\)", "]", cuerpo)


def rel_a(desde, hacia):
    return posixpath.relpath(hacia, posixpath.dirname(desde) or ".")


def poner_bloque(texto, nombre, contenido):
    """Reemplaza el bloque automático en su sitio. Si no existe, lo añade al final."""
    bloque = f"<!-- auto:{nombre} -->\n{contenido.strip()}\n<!-- /auto:{nombre} -->"
    patron = re.compile(rf"<!-- auto:{nombre} -->.*?<!-- /auto:{nombre} -->", re.S)
    if patron.search(texto):
        return patron.sub(lambda m: bloque, texto, count=1)
    return texto.rstrip() + "\n\n" + bloque + "\n"


def poner_bloque_tras_titulo(texto, nombre, contenido):
    """Como poner_bloque, pero si el bloque no existe lo coloca justo después del título (#)."""
    bloque = f"<!-- auto:{nombre} -->\n{contenido.strip()}\n<!-- /auto:{nombre} -->"
    patron = re.compile(rf"<!-- auto:{nombre} -->.*?<!-- /auto:{nombre} -->", re.S)
    if patron.search(texto):
        return patron.sub(lambda m: bloque, texto, count=1)
    fm_fin = FM_RE.match(texto)
    inicio = fm_fin.end() if fm_fin else 0
    m = re.search(r"^# .*$", texto[inicio:], re.M)
    if not m:
        return texto.rstrip() + "\n\n" + bloque + "\n"
    pos = inicio + m.end()
    return texto[:pos] + "\n\n" + bloque + texto[pos:]


def quitar_bloque(texto, nombre):
    return re.sub(rf"\n*<!-- auto:{nombre} -->.*?<!-- /auto:{nombre} -->\n*", "\n", texto, flags=re.S)


def slug_ancla(texto):
    """Ancla de un encabezado, con la misma lógica básica que GitHub."""
    texto = re.sub(r"[`*_]", "", texto.strip().lower())
    texto = re.sub(r"[^\w\- ]", "", texto)
    return texto.replace(" ", "-")


def resumen_de(texto, max_chars=180):
    """Primera frase de prosa de una nota. Sirve para listas compactas."""
    cuerpo = re.sub(r"```.*?```", "", prosa(texto), flags=re.S)
    for linea in cuerpo.split("\n"):
        linea = linea.strip()
        if not linea or linea.startswith(("#", "- ", "* ", "|", "<", ">", "!", "---")) or re.match(r"\d+\.\s", linea):
            continue
        if PENDIENTE in linea:
            continue
        linea = re.sub(r"\]\([^)]*\)", "]", linea)
        linea = re.sub(r"\[([^\]]*)\]", r"\1", linea)
        linea = re.sub(r"[*_`]", "", linea).strip()
        if not linea:
            continue
        frase = re.split(r"(?<=[.!?])\s", linea, maxsplit=1)[0]
        return frase[:max_chars].rstrip() + ("…" if len(frase) > max_chars else "")
    return ""


def _texto_plano(t):
    """Título sin enlaces ni formato, como lo muestra GitHub."""
    t = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", t)
    return re.sub(r"[`*_]", "", t).strip()


def _norm(t):
    """Minúsculas y sin tildes, para comparar términos."""
    return "".join(ch for ch in unicodedata.normalize("NFD", str(t)) if unicodedata.category(ch) != "Mn").lower()


def anclas_de(texto):
    """Anclas de todos los encabezados, como GitHub: el repetido recibe -1, -2, ..."""
    usados, salida = Counter(), set()
    for m in re.finditer(r"^#{1,6}\s+(.+)$", sin_bloques(texto), re.M):
        base = slug_ancla(_texto_plano(m.group(1)))
        salida.add(base if usados[base] == 0 else f"{base}-{usados[base]}")
        usados[base] += 1
    return salida


def _secciones(texto):
    """Secciones H2 de una lección con su ancla."""
    cuerpo = prosa(texto)
    usados, cabeceras, salida = Counter(), list(re.finditer(r"^(#{1,6})\s+(.+)$", cuerpo, re.M)), []
    for i, m in enumerate(cabeceras):
        titulo = _texto_plano(m.group(2))
        base = slug_ancla(titulo)
        ancla = base if usados[base] == 0 else f"{base}-{usados[base]}"
        usados[base] += 1
        if len(m.group(1)) != 2:
            continue
        salida.append({"titulo": titulo, "ancla": ancla})
    return salida


def _celda(t):
    return str(t).replace("|", "/").strip()


def palabras(texto):
    """Número de palabras de la prosa de una nota, sin código, enlaces técnicos ni bloques automáticos."""
    cuerpo = re.sub(r"<!--.*?-->", " ", prosa(texto), flags=re.S)
    cuerpo = re.sub(r"```.*?```", " ", cuerpo, flags=re.S)
    cuerpo = re.sub(r"^#+\s.*$", " ", cuerpo, flags=re.M)
    return len(re.findall(r"\w+", cuerpo))


# ------------------------------------------------------------------ conceptos

def cargar_conceptos(raiz):
    """Conceptos = archivos .md dentro de conceptos/ que no son categoria.md."""
    conceptos = {}
    for rel in documentos(raiz):
        if not rel.startswith("conceptos/") or Path(rel).name == "categoria.md":
            continue
        fm, _ = leer_frontmatter((raiz / rel).read_text(encoding="utf-8"))
        slug = Path(rel).stem
        titulo = fm.get("titulo", slug)
        aliases = list(dict.fromkeys([titulo] + fm.get("aliases", [])))
        conceptos[slug] = {"titulo": titulo, "aliases": aliases, "ruta": rel, "categoria": fm.get("categoria", "")}
    return conceptos


def compilar_terminos(conceptos):
    """Un solo patrón para todos los términos. Gana el alias más largo.
    Se usa solo para contar menciones de conceptos en las lecciones (grafo.json)."""
    pares = sorted(
        ((alias, slug) for slug, c in conceptos.items() for alias in c["aliases"]),
        key=lambda p: -len(p[0]),
    )
    alternativas, buscar = [], {}
    for alias, slug in pares:
        if alias.isupper():
            alternativas.append("(?-i:" + re.escape(alias) + ")")
            buscar.setdefault(alias, slug)
        else:
            alternativas.append("(?i:" + re.escape(alias) + ")")
            buscar.setdefault(alias.lower(), slug)
    patron = re.compile(r"(?<!\w)(?:" + "|".join(alternativas) + r")(?!\w)")
    return patron, buscar


def slug_de(texto, buscar):
    return buscar.get(texto) or buscar.get(texto.lower())


def contar_menciones(texto, patron, buscar):
    cuenta = Counter()
    for m in patron.finditer(texto):
        slug = slug_de(m.group(0), buscar)
        if slug:
            cuenta[slug] += 1
    return cuenta


# ------------------------------------------------------------------ regenerar

def regenerar(raiz=RAIZ):
    AREAS = areas(raiz)
    CATS = categorias(raiz)
    conceptos = cargar_conceptos(raiz)
    patron, buscar = compilar_terminos(conceptos)

    docs = {}
    for rel in documentos(raiz):
        texto = (raiz / rel).read_text(encoding="utf-8")
        docs[rel] = {"texto": texto, "fm": leer_frontmatter(texto)[0]}

    def titulo(r):
        return docs[r]["fm"]["titulo"]

    lecciones = sorted(
        (r for r in docs if "orden" in docs[r]["fm"] and docs[r]["fm"].get("area") in AREAS),
        key=lambda r: (AREAS[docs[r]["fm"]["area"]]["orden"], int(docs[r]["fm"]["orden"])),
    )
    grupos = defaultdict(list)
    for r in lecciones:
        grupos[docs[r]["fm"]["area"]].append(r)
    menciones = {r: contar_menciones(cuerpo_visible(docs[r]["texto"]), patron, buscar) for r in lecciones}

    # Pie de cada lección: solo navegación. Las conexiones entre conceptos se escriben a mano.
    for r in lecciones:
        area = docs[r]["fm"]["area"]
        g = grupos[area]
        k = g.index(r)
        nav = []
        if k > 0:
            nav.append(f"[← Anterior: {titulo(g[k - 1])}]({rel_a(r, g[k - 1])})")
        nav.append(f"[Índice de {AREAS[area]['nombre']}]({rel_a(r, AREAS[area]['indice'])})")
        if k < len(g) - 1:
            nav.append(f"[Siguiente: {titulo(g[k + 1])} →]({rel_a(r, g[k + 1])})")
        docs[r]["texto"] = poner_bloque(docs[r]["texto"], "pie", "---\n\n**Navegación:** " + " · ".join(nav))

    # Conceptos: quitar bloques antiguos y señalar la categoría justo debajo del título.
    for c, datos in conceptos.items():
        r = datos["ruta"]
        docs[r]["texto"] = quitar_bloque(docs[r]["texto"], "backlinks")
        cat = datos["categoria"]
        if cat in CATS:
            enlace = rel_a(r, CATS[cat]["indice"])
            docs[r]["texto"] = poner_bloque_tras_titulo(
                docs[r]["texto"], "categoria", f"Categoría: [{nombre_categoria(CATS, cat)}]({enlace})"
            )

    # Índice de cada categoría: subcategorías y conceptos directos.
    for ruta, cat in CATS.items():
        indice = cat["indice"]
        partes = []
        subs = hijas(CATS, ruta)
        if subs:
            partes.append("## Subcategorías\n\n" + "\n".join(
                f"- [{CATS[s]['nombre']}]({rel_a(indice, CATS[s]['indice'])})" for s in subs))
        directos = sorted(
            (c for c, d in conceptos.items() if d["categoria"] == ruta),
            key=lambda c: conceptos[c]["titulo"].lower(),
        )
        lista = "\n".join(
            f"- [{conceptos[c]['titulo']}]({rel_a(indice, conceptos[c]['ruta'])}): "
            f"{resumen_de(docs[conceptos[c]['ruta']]['texto'])}"
            for c in directos
        ) or "Todavía no hay conceptos en esta categoría."
        partes.append("## Conceptos\n\n" + lista)
        docs[indice]["texto"] = poner_bloque(docs[indice]["texto"], "contenido", "\n\n".join(partes))

    # Índices de área.
    for area, datos in AREAS.items():
        ruta = datos["indice"]
        if ruta in docs:
            lista = "\n".join(f"{i}. [{titulo(l)}]({rel_a(ruta, l)})" for i, l in enumerate(grupos[area], 1))
            docs[ruta]["texto"] = poner_bloque(
                docs[ruta]["texto"], "lecciones", "## Lecciones\n\n" + (lista or "Todavía no hay lecciones.")
            )

    # Áreas y categorías en el README.
    if "README.md" in docs:
        lista = "\n".join(
            f"{i}. [{d['nombre']}]({rel_a('README.md', d['indice'])}): {len(grupos[a])} lecciones"
            for i, (a, d) in enumerate(AREAS.items(), 1)
        )
        docs["README.md"]["texto"] = poner_bloque(docs["README.md"]["texto"], "areas", lista)

        def total(ruta):
            return sum(1 for d in conceptos.values() if d["categoria"] == ruta or d["categoria"].startswith(ruta + "/"))

        cats_top = hijas(CATS, None)
        lista = "\n".join(
            f"{i}. [{CATS[r]['nombre']}]({rel_a('README.md', CATS[r]['indice'])}): {total(r)} conceptos"
            for i, r in enumerate(cats_top, 1)
        )
        docs["README.md"]["texto"] = poner_bloque(docs["README.md"]["texto"], "categorias", lista)

    # Mapa de contenidos.
    if "MAPA.md" in docs:
        partes = []
        for area, datos in AREAS.items():
            if grupos[area]:
                items = "\n".join(f"{i}. [{titulo(l)}]({rel_a('MAPA.md', l)})" for i, l in enumerate(grupos[area], 1))
                partes.append(f"## {datos['nombre']}\n\n{items}")

        def bloque_categoria(ruta, nivel):
            cabecera = "#" * nivel + " " + CATS[ruta]["nombre"]
            directos = sorted(
                (c for c, d in conceptos.items() if d["categoria"] == ruta),
                key=lambda c: conceptos[c]["titulo"].lower(),
            )
            cuerpo = "\n".join(f"- [{conceptos[c]['titulo']}]({rel_a('MAPA.md', conceptos[c]['ruta'])})" for c in directos)
            bloques = [cabecera + ("\n\n" + cuerpo if cuerpo else "")]
            for s in hijas(CATS, ruta):
                bloques.append(bloque_categoria(s, nivel + 1))
            return "\n\n".join(bloques)

        partes.append("## Conceptos\n\n" + "\n\n".join(bloque_categoria(r, 3) for r in hijas(CATS, None)))
        docs["MAPA.md"]["texto"] = poner_bloque(docs["MAPA.md"]["texto"], "mapa", "\n\n".join(partes))

    for rel, d in docs.items():
        (raiz / rel).write_text(d["texto"], encoding="utf-8")

    generar_cerebro(raiz, AREAS, CATS, conceptos, docs, grupos, menciones)

    # Grafo de la red en formato de datos (para herramientas, no para Obsidian).
    nodos, aristas = [], []
    for r in lecciones:
        fm = docs[r]["fm"]
        nodos.append({"id": r, "tipo": "leccion", "titulo": fm["titulo"], "area": fm["area"], "orden": int(fm["orden"])})
        for c, n in menciones[r].items():
            aristas.append({"origen": r, "destino": conceptos[c]["ruta"], "tipo": "menciona", "peso": n})
    for a, b in zip(lecciones, lecciones[1:]):
        if docs[a]["fm"]["area"] == docs[b]["fm"]["area"]:
            aristas.append({"origen": a, "destino": b, "tipo": "sigue_a", "peso": 1})
    for c, datos in conceptos.items():
        nodos.append({"id": datos["ruta"], "tipo": "concepto", "titulo": datos["titulo"],
                      "categoria": datos["categoria"], "alias": datos["aliases"]})
    (raiz / "grafo.json").write_text(
        json.dumps({"nodos": nodos, "aristas": aristas}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def generar_cerebro(raiz, AREAS, CATS, conceptos, docs, grupos, menciones):
    """Escribe dos archivos de búsqueda:
    - cerebro/inicio.md: acceso rápido y todos los conceptos agrupados por categoría.
    - cerebro/lecciones.md: cada lección con sus secciones (H2)."""
    carpeta = raiz / "cerebro"
    carpeta.mkdir(exist_ok=True)
    for viejo in carpeta.glob("*.md"):
        viejo.unlink()
    origen = "cerebro/inicio.md"

    L = [
        "# Inicio: mapa rápido de los apuntes", "",
        "Índice para buscar con Ctrl+F: escribe el concepto o el tema, en español o en inglés, y sigue el enlace. "
        "Se genera solo con `actualizar`; no lo edites a mano.", "",
        "## Acceso rápido", "",
        "| Quiero... | Ir a |", "| --- | --- |",
        f"| Empezar a estudiar | [Bases de datos]({rel_a(origen, 'bases-de-datos/indice.md')}) |",
        f"| Buscar una sección de una lección | [Lecciones por secciones]({rel_a(origen, 'cerebro/lecciones.md')}) |",
        f"| Ver el mapa completo | [Mapa de contenidos]({rel_a(origen, 'MAPA.md')}) |",
        f"| Consultar con Gemini | [Tutorial de Gemini]({rel_a(origen, 'consultar-con-gemini.md')}) |",
        f"| Consultar sin conexión | [Tutorial de Ollama]({rel_a(origen, 'tutorial-ollama.md')}) |",
        f"| Añadir o mantener contenido | [Guía de mantenimiento]({rel_a(origen, 'MANTENIMIENTO.md')}) |",
        "", "## Conceptos por categoría", "",
    ]
    def en_orden(padre=None):
        """Categorías en el mismo orden del árbol que el mapa: padre, luego sus hijas."""
        for r in hijas(CATS, padre):
            yield r
            yield from en_orden(r)

    for ruta in en_orden():
        directos = sorted(
            (c for c, d in conceptos.items() if d["categoria"] == ruta),
            key=lambda c: conceptos[c]["titulo"].lower(),
        )
        if not directos:
            continue
        descripcion = resumen_de(docs[CATS[ruta]["indice"]]["texto"], max_chars=300)
        L += [f"### [{nombre_categoria(CATS, ruta)}]({rel_a(origen, CATS[ruta]['indice'])})", ""]
        if descripcion:
            L += [f"> {descripcion}", ""]
        L += ["| Concepto | Qué es |", "| --- | --- |"]
        for c in directos:
            d = conceptos[c]
            L.append(f"| [{_celda(d['titulo'])}]({rel_a(origen, d['ruta'])}) | "
                     f"{_celda(resumen_de(docs[d['ruta']]['texto'], max_chars=170))} |")
        L.append("")
    cabecera = '---\ntitulo: "Inicio: mapa rápido de los apuntes"\ntags: ["cerebro"]\n---\n\n'
    (carpeta / "inicio.md").write_text(cabecera + "\n".join(L).rstrip() + "\n", encoding="utf-8")

    origen2 = "cerebro/lecciones.md"
    M = ["# Lecciones por secciones", "",
         "Índice de cada lección con sus secciones. Para ubicar un concepto, empieza por [Inicio](inicio.md).", ""]
    for area, datos in AREAS.items():
        if not grupos[area]:
            continue
        M += [f"## {datos['nombre']}", "", f"Índice: [{datos['nombre']}]({rel_a(origen2, datos['indice'])})", ""]
        for i, l in enumerate(grupos[area], 1):
            M.append(f"### {i:02d} · [{docs[l]['fm']['titulo']}]({rel_a(origen2, l)})")
            M += [f"- [{sec['titulo']}]({rel_a(origen2, l)}#{sec['ancla']})" for sec in _secciones(docs[l]["texto"])]
            M.append("")
    cabecera2 = '---\ntitulo: "Lecciones por secciones"\ntags: ["cerebro"]\n---\n\n'
    (carpeta / "lecciones.md").write_text(cabecera2 + "\n".join(M).rstrip() + "\n", encoding="utf-8")


# ------------------------------------------------------------------ validar

ENLACE_RE_VALIDAR = ENLACE_RE


def validar(raiz=RAIZ):
    errores, avisos = [], []
    AREAS = areas(raiz)
    CATS = categorias(raiz)
    conceptos = cargar_conceptos(raiz)
    rels = documentos(raiz)
    existentes = {p.relative_to(raiz).as_posix() for p in raiz.rglob("*") if p.is_file()}
    textos = {r: (raiz / r).read_text(encoding="utf-8") for r in rels}
    anclas = {r: anclas_de(textos[r]) for r in rels}

    # Áreas de lecciones: toda carpeta de contenido debe ser un área declarada.
    for carpeta in {p.parent.name for p in raiz.glob("*/*.md")} - CARPETAS_ESPECIALES:
        if carpeta not in AREAS:
            errores.append(f"{carpeta}/: carpeta de contenido sin indice.md válido (necesita 'area' y 'area_orden')")

    # Categorías de conceptos: cada carpeta de conceptos/ debe tener categoria.md y cada concepto debe estar en la suya.
    for carpeta in (raiz / "conceptos").rglob("*"):
        if carpeta.is_dir() and any(carpeta.glob("*.md")) and not (carpeta / "categoria.md").exists():
            errores.append(f"{carpeta.relative_to(raiz).as_posix()}/: falta categoria.md")
    for ruta, cat in CATS.items():
        fm, _ = leer_frontmatter(textos[cat["indice"]])
        if fm.get("categoria") != ruta:
            errores.append(f"{cat['indice']}: 'categoria' debe ser '{ruta}'")
        if cat["padre"] and cat["padre"] not in CATS:
            errores.append(f"{cat['indice']}: la categoría padre '{cat['padre']}' no existe")

    # Alias: ningún término puede señalar dos conceptos distintos.
    vistos = {}
    for slug, c in conceptos.items():
        for alias in c["aliases"]:
            clave = _norm(alias).strip()
            if clave in vistos and vistos[clave] != slug:
                errores.append(f"alias '{alias}' usado por dos conceptos: {vistos[clave]} y {slug}")
            vistos.setdefault(clave, slug)

    for slug, c in conceptos.items():
        r = c["ruta"]
        fm, _ = leer_frontmatter(textos[r])
        if "titulo" not in fm:
            errores.append(f"{r}: falta 'titulo' en el frontmatter")
        if c["categoria"] not in CATS:
            errores.append(f"{r}: categoria '{c['categoria']}' no existe")
        elif posixpath.dirname(r)[len("conceptos/"):] != c["categoria"]:
            errores.append(f"{r}: debe estar en la carpeta 'conceptos/{c['categoria']}/'")
        if PENDIENTE in sin_codigo(textos[r]):
            errores.append(f"{r}: queda una línea '{PENDIENTE}' por completar")
        if palabras(textos[r]) < MIN_PALABRAS_CONCEPTO:
            avisos.append(f"{r}: concepto breve ({palabras(textos[r])} palabras; conviene al menos {MIN_PALABRAS_CONCEPTO})")
        if not re.search(r"^## ", sin_bloques(textos[r]), re.M):
            avisos.append(f"{r}: no tiene secciones (##)")

    for ruta_cat, cat in CATS.items():
        fm, _ = leer_frontmatter(textos[cat["indice"]])
        if "nombre" not in fm or "orden" not in fm:
            errores.append(f"{cat['indice']}: faltan 'nombre' y 'orden' en el frontmatter")

    for r in rels:
        texto = textos[r]
        fm, _ = leer_frontmatter(texto)
        cuerpo = sin_bloques(texto)

        if "titulo" not in fm:
            errores.append(f"{r}: falta 'titulo' en el frontmatter")
        if "area" in fm and "orden" in fm:
            if fm.get("area") not in AREAS:
                errores.append(f"{r}: área '{fm.get('area')}' no declarada")
            elif not r.startswith(fm["area"] + "/"):
                errores.append(f"{r}: la lección debe estar en la carpeta '{fm['area']}/'")
        if PENDIENTE in sin_codigo(texto):
            errores.append(f"{r}: queda una línea '{PENDIENTE}' por completar")

        niveles = [len(m.group(1)) for m in re.finditer(r"^(#{1,6})\s", cuerpo, re.M)]
        if niveles.count(1) != 1:
            errores.append(f"{r}: tiene {niveles.count(1)} encabezados H1 (debe tener exactamente 1)")
        previo = 0
        for n in niveles:
            if n > previo + 1:
                errores.append(f"{r}: salto de encabezado (nivel {n} después de nivel {previo})")
                break
            previo = n

        nombre = Path(r).name
        if nombre not in RAIZ_MAYUSCULAS and not re.fullmatch(r"(\d{2}-)?" + SLUG_RE.pattern + r"\.md", nombre):
            if not r.startswith("conceptos/"):
                errores.append(f"{r}: nombre de archivo no válido (minúsculas, guiones, sin espacios)")
        if "[[" in sin_codigo(texto):
            errores.append(f"{r}: contiene wikilinks [[...]]; usa enlaces Markdown")

        for m in ENLACE_RE.finditer(sin_codigo(texto)):
            destino = m.group(3)
            if destino.startswith(("http://", "https://", "mailto:")):
                continue
            ruta, _, ancla = destino.partition("#")
            if not ruta:
                if ancla and slug_ancla(ancla) not in anclas[r]:
                    errores.append(f"{r}: ancla inexistente → {destino}")
                continue
            objetivo = posixpath.normpath(posixpath.join(posixpath.dirname(r) or ".", unquote(ruta)))
            if objetivo not in existentes:
                errores.append(f"{r}: enlace roto → {destino}")
                continue
            if ancla and objetivo in anclas and slug_ancla(ancla) not in anclas[objetivo]:
                errores.append(f"{r}: ancla inexistente → {destino}")

    # Conceptos que nadie enlaza: aviso para decidir si se completan, se fusionan o se borran.
    texto_total = "\n".join(textos[r] for r in rels if not r.startswith("cerebro/"))
    for slug, c in conceptos.items():
        if not re.search(r"(?<![\w-])" + re.escape(Path(c["ruta"]).name) + r"\)", texto_total) and \
           not re.search(r"(?<![\w-])" + re.escape(Path(c["ruta"]).name) + r"#", texto_total):
            avisos.append(f"concepto sin enlaces desde ninguna otra nota: {c['ruta']}")

    tokens_cerebro = {}
    for r in rels:
        tokens = len(textos[r]) // 4
        if r.startswith("cerebro/"):
            tokens_cerebro[r] = tokens
    for r, tokens in tokens_cerebro.items():
        if tokens > 8000:
            avisos.append(f"{r}: ~{tokens} tokens; es grande para un modelo local, pero sirve para Gemini")
    grandes = [r for r in rels if "area" in leer_frontmatter(textos[r])[0] and "orden" in leer_frontmatter(textos[r])[0] and len(textos[r]) // 4 > 6000]
    if grandes:
        avisos.append(f"{len(grandes)} lecciones superan ~6000 tokens. En el chat usa 'Current selection' "
                      f"sobre la sección que necesites, no la nota completa.")

    for a in avisos:
        print("AVISO   ", a)
    for e in errores:
        print("ERROR   ", e)
    print(f"\n{len(rels)} documentos, {len(conceptos)} conceptos, {len(CATS)} categorías, {len(AREAS)} áreas. "
          f"Errores: {len(errores)}. Avisos: {len(avisos)}.")
    return 1 if errores else 0


# ------------------------------------------------------------------ crear archivos

def _slug_valido(slug):
    if not SLUG_RE.fullmatch(slug):
        raise ValueError(f"'{slug}' no es válido: usa minúsculas, números y guiones (ej. 'mi-tema').")


def crear_area(raiz, slug, nombre, orden):
    _slug_valido(slug)
    carpeta = raiz / slug
    if carpeta.exists():
        raise ValueError(f"ya existe la carpeta '{slug}/'.")
    carpeta.mkdir()
    datos = {"titulo": f"Índice de {nombre}", "nombre": nombre, "area": slug, "area_orden": int(orden), "tags": [slug]}
    (carpeta / "indice.md").write_text(
        fm_texto(datos) + f"# Índice de {nombre}\n\n{PENDIENTE} describe el área en una o dos frases.\n", encoding="utf-8")
    return carpeta / "indice.md"


def crear_categoria(raiz, ruta, nombre, orden):
    partes = ruta.split("/")
    for p in partes:
        _slug_valido(p)
    carpeta = raiz / "conceptos" / ruta
    if (carpeta / "categoria.md").exists():
        raise ValueError(f"ya existe la categoría '{ruta}'.")
    padre = "/".join(partes[:-1])
    if padre and not (raiz / "conceptos" / padre / "categoria.md").exists():
        raise ValueError(f"la categoría padre '{padre}' no existe. Créala primero.")
    carpeta.mkdir(parents=True, exist_ok=True)
    datos = {"titulo": f"Categoría: {nombre}", "categoria": ruta, "nombre": nombre, "orden": int(orden), "tags": ["categoria"]}
    (carpeta / "categoria.md").write_text(
        fm_texto(datos) + f"# {nombre}\n\n{PENDIENTE} describe qué conceptos reúne esta categoría y por qué.\n",
        encoding="utf-8")
    return carpeta / "categoria.md"


def crear_leccion(raiz, area, orden, slug, titulo):
    AREAS = areas(raiz)
    if area not in AREAS:
        raise ValueError(f"el área '{area}' no existe. Áreas: {', '.join(AREAS)}.")
    _slug_valido(slug)
    ruta = raiz / area / f"{int(orden):02d}-{slug}.md"
    if ruta.exists():
        raise ValueError(f"ya existe {ruta.relative_to(raiz).as_posix()}.")
    datos = {"titulo": titulo, "area": area, "orden": int(orden), "tags": [area]}
    ruta.write_text(fm_texto(datos) + f"# {titulo}\n\n{PENDIENTE} escribe aquí el contenido de la lección.\n", encoding="utf-8")
    return ruta


def crear_concepto(raiz, slug, titulo, aliases, categoria):
    _slug_valido(slug)
    cats = categorias(raiz)
    if categoria not in cats:
        raise ValueError(f"la categoría '{categoria}' no existe. Categorías: {', '.join(cats)}.")
    ruta = raiz / "conceptos" / categoria / f"{slug}.md"
    if ruta.exists() or (raiz / "conceptos" / f"{slug}.md").exists():
        raise ValueError(f"ya existe un concepto llamado '{slug}'.")
    lista = list(dict.fromkeys([titulo] + [a.strip() for a in aliases if a.strip()]))
    datos = {"titulo": titulo, "aliases": lista, "categoria": categoria, "tags": ["concepto"]}
    cuerpo = (f"# {titulo}\n\n<!-- auto:categoria -->\n<!-- /auto:categoria -->\n\n"
              f"{PENDIENTE} escribe la definición en una o dos frases.\n\n"
              "## Cómo funciona\n\nDesarrolla el concepto con ejemplos.\n")
    ruta.write_text(fm_texto(datos) + cuerpo, encoding="utf-8")
    return ruta


# ------------------------------------------------------------------ CLI

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, args = argv[1], argv[2:]
    try:
        if cmd == "actualizar":
            regenerar()
            print("Índices, categorías, mapa, cerebro y grafo.json regenerados.")
            return validar()
        if cmd == "regenerar":
            regenerar()
            print("Índices, categorías, mapa, cerebro y grafo.json regenerados.")
            return 0
        if cmd == "validar":
            return validar()
        if cmd == "nueva-area" and len(args) == 3:
            print("Creado:", crear_area(RAIZ, args[0], args[1], args[2]).relative_to(RAIZ).as_posix())
            print("Siguiente paso: escribe el índice, luego ejecuta 'actualizar'.")
            return 0
        if cmd == "nueva-leccion" and len(args) == 4:
            print("Creado:", crear_leccion(RAIZ, args[0], args[1], args[2], args[3]).relative_to(RAIZ).as_posix())
            print("Siguiente paso: escribe la lección, luego ejecuta 'actualizar'.")
            return 0
        if cmd == "nueva-categoria" and len(args) == 3:
            print("Creado:", crear_categoria(RAIZ, args[0], args[1], args[2]).relative_to(RAIZ).as_posix())
            print("Siguiente paso: escribe la descripción, luego ejecuta 'actualizar'.")
            return 0
        if cmd == "nuevo-concepto" and len(args) == 4:
            aliases = args[2].split("|") if args[2] else []
            print("Creado:", crear_concepto(RAIZ, args[0], args[1], aliases, args[3]).relative_to(RAIZ).as_posix())
            print("Siguiente paso: escribe la definición y el contenido, luego ejecuta 'actualizar'.")
            return 0
    except ValueError as e:
        print("ERROR   ", e)
        return 2
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
