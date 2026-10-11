#!/usr/bin/env python3
"""Mantenimiento de los apuntes. Ejecútalo desde la raíz del repositorio (Python 3.8 o superior).

  python3 herramientas/mantenimiento.py actualizar
      Enlaza conceptos, regenera índices, mapas, cerebro y grafo, y valida.
      Es el comando que hay que ejecutar después de cualquier cambio.

  python3 herramientas/mantenimiento.py nueva-area SLUG "Nombre" ORDEN
  python3 herramientas/mantenimiento.py nueva-leccion AREA ORDEN SLUG "Título"
  python3 herramientas/mantenimiento.py nuevo-concepto SLUG "Título" "alias1|alias2"
      Crean archivos con su estructura. Cada uno trae una línea PENDIENTE: que hay que reemplazar.

  python3 herramientas/mantenimiento.py enlazar | regenerar | validar
      Pasos sueltos de "actualizar".

Los bloques entre <!-- auto:nombre --> y <!-- /auto:nombre --> se generan solos. No los edites.
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
    """Áreas = carpetas con indice.md que declara 'area' y 'area_orden'. Ordenadas por 'area_orden'."""
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


def slug_ancla(texto):
    """Ancla de un encabezado, con la misma lógica básica que GitHub."""
    texto = re.sub(r"[`*_]", "", texto.strip().lower())
    texto = re.sub(r"[^\w\- ]", "", texto)
    return texto.replace(" ", "-")


def resumen_de(texto, max_chars=180):
    """Primera frase de prosa de una nota. Sirve para glosarios y listas compactas."""
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


# ------------------------------------------------------------------ conceptos y términos

def cargar_conceptos(raiz):
    conceptos = {}
    for rel in documentos(raiz):
        if not rel.startswith("conceptos/"):
            continue
        fm, _ = leer_frontmatter((raiz / rel).read_text(encoding="utf-8"))
        slug = Path(rel).stem
        titulo = fm.get("titulo", slug)
        aliases = list(dict.fromkeys([titulo] + fm.get("aliases", [])))
        conceptos[slug] = {"titulo": titulo, "aliases": aliases, "ruta": rel}
    return conceptos


def compilar_terminos(conceptos):
    """Un solo patrón para todos los términos. Gana el alias más largo (así 'llaves foráneas' no se confunde con 'llaves').
    Las siglas (todo en mayúsculas) distinguen mayúsculas; el resto no."""
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


def _es_contenido_enlazable(rel, fm):
    """Lecciones y conceptos reciben enlaces automáticos. Índices, cerebro y raíz no."""
    return rel.startswith("conceptos/") or "orden" in fm


# ------------------------------------------------------------------ enlazar

def _conceptos_ya_enlazados(cuerpo, rel):
    """Slugs de concepto que el documento ya enlaza, sin importar cómo esté escrita la ruta."""
    base = posixpath.dirname(rel) or "."
    slugs = set()
    for m in ENLACE_RE.finditer(BLOQUE_AUTO_RE.sub("\n", cuerpo)):
        destino = m.group(3).split("#")[0]
        if not destino or destino.startswith(("http://", "https://", "mailto:")):
            continue
        objetivo = posixpath.normpath(posixpath.join(base, unquote(destino)))
        if objetivo.startswith("conceptos/") and objetivo.endswith(".md"):
            slugs.add(Path(objetivo).stem)
    return slugs


def _enlazar_cuerpo(cuerpo, rel, propio, patron, buscar):
    """Enlaza la primera mención de cada concepto. Respeta código, enlaces, encabezados y bloques automáticos."""
    hechos = _conceptos_ya_enlazados(cuerpo, rel)
    if propio:
        hechos.add(propio)
    base = posixpath.dirname(rel) or "."
    salida, en_codigo, en_auto, n = [], False, False, 0
    for linea in cuerpo.split("\n"):
        s = linea.lstrip()
        if s.startswith("<!-- auto:"):
            en_auto = True
        if en_auto:
            salida.append(linea)
            if s.startswith("<!-- /auto:"):
                en_auto = False
            continue
        if s.startswith("```"):
            en_codigo = not en_codigo
            salida.append(linea)
            continue
        if en_codigo or s.startswith(("#", "<!--")):
            salida.append(linea)
            continue
        partes = PROT_RE.split(linea)
        nuevas = []
        for i, parte in enumerate(partes):
            if i % 2 == 1:
                nuevas.append(parte)
                continue
            pos, out = 0, []
            for m in patron.finditer(parte):
                slug = slug_de(m.group(0), buscar)
                if not slug or slug in hechos:
                    continue
                hechos.add(slug)
                out.append(parte[pos:m.start()])
                out.append(f"[{m.group(0)}]({posixpath.relpath(f'conceptos/{slug}.md', base)})")
                pos = m.end()
                n += 1
            out.append(parte[pos:])
            nuevas.append("".join(out))
        salida.append("".join(nuevas))
    return "\n".join(salida), n


def enlazar(raiz=RAIZ):
    conceptos = cargar_conceptos(raiz)
    patron, buscar = compilar_terminos(conceptos)
    total = 0
    for rel in documentos(raiz):
        p = raiz / rel
        texto = p.read_text(encoding="utf-8")
        fm, cuerpo = leer_frontmatter(texto)
        if not _es_contenido_enlazable(rel, fm):
            continue
        propio = Path(rel).stem if rel.startswith("conceptos/") else None
        nuevo, n = _enlazar_cuerpo(cuerpo, rel, propio, patron, buscar)
        if n:
            total += n
            p.write_text(texto[: len(texto) - len(cuerpo)] + nuevo, encoding="utf-8")
    return total


# ------------------------------------------------------------------ regenerar

def regenerar(raiz=RAIZ):
    AREAS = areas(raiz)
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

    # Pie de cada lección: navegación y conceptos.
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
        top = [c for c, _ in menciones[r].most_common(15)]
        conc = ", ".join(f"[{conceptos[c]['titulo']}]({rel_a(r, conceptos[c]['ruta'])})" for c in top)
        contenido = "---\n\n**Navegación:** " + " · ".join(nav) + "\n\n**Conceptos de esta lección:** " + (conc or "ninguno")
        docs[r]["texto"] = poner_bloque(docs[r]["texto"], "pie", contenido)

    # Cada concepto: dónde aparece y qué conceptos le acompañan (con su resumen).
    donde = defaultdict(list)
    junto = defaultdict(Counter)
    for r in lecciones:
        m = menciones[r]
        for c, n in m.items():
            donde[c].append((r, n))
            junto[c].update(t for t in m if t != c)
    for c, datos in conceptos.items():
        r = datos["ruta"]
        if r not in docs:
            continue
        items = sorted(donde[c], key=lambda x: (-x[1], titulo(x[0])))
        lista = "\n".join(
            f"- [{titulo(l)}]({rel_a(r, l)}) · {AREAS[docs[l]['fm']['area']]['nombre']} · "
            f"{n} {'mención' if n == 1 else 'menciones'}"
            for l, n in items
        ) or "Todavía no aparece en ninguna lección."
        vecinos = [t for t, _ in junto[c].most_common(6)]
        cerca = "\n".join(
            f"- [{conceptos[t]['titulo']}]({rel_a(r, conceptos[t]['ruta'])}): {resumen_de(docs[conceptos[t]['ruta']]['texto'])}"
            for t in vecinos
        )
        contenido = f"## Dónde aparece\n\n{lista}\n\n## Conceptos cercanos\n\n{cerca or 'Ninguno todavía.'}"
        docs[r]["texto"] = poner_bloque(docs[r]["texto"], "backlinks", contenido)

    # Índices de área.
    for area, datos in AREAS.items():
        ruta = datos["indice"]
        if ruta in docs:
            lista = "\n".join(f"{i}. [{titulo(l)}]({rel_a(ruta, l)})" for i, l in enumerate(grupos[area], 1))
            docs[ruta]["texto"] = poner_bloque(
                docs[ruta]["texto"], "lecciones", "## Lecciones\n\n" + (lista or "Todavía no hay lecciones.")
            )

    # Lista de áreas en el README.
    if "README.md" in docs:
        lista = "\n".join(
            f"{i}. [{d['nombre']}]({rel_a('README.md', d['indice'])}): {len(grupos[a])} lecciones"
            for i, (a, d) in enumerate(AREAS.items(), 1)
        )
        docs["README.md"]["texto"] = poner_bloque(docs["README.md"]["texto"], "areas", lista)

    # Mapa de contenidos.
    if "MAPA.md" in docs:
        partes = []
        for area, datos in AREAS.items():
            if grupos[area]:
                items = "\n".join(f"{i}. [{titulo(l)}]({rel_a('MAPA.md', l)})" for i, l in enumerate(grupos[area], 1))
                partes.append(f"## {datos['nombre']}\n\n{items}")
        conc = "\n".join(
            f"- [{c['titulo']}]({rel_a('MAPA.md', c['ruta'])})"
            for c in sorted(conceptos.values(), key=lambda c: c["titulo"].lower())
        )
        partes.append(f"## Conceptos\n\n{conc}")
        docs["MAPA.md"]["texto"] = poner_bloque(docs["MAPA.md"]["texto"], "mapa", "\n\n".join(partes))

    for rel, d in docs.items():
        (raiz / rel).write_text(d["texto"], encoding="utf-8")

    generar_cerebro(raiz, AREAS, conceptos, docs, grupos, menciones)

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
        nodos.append({"id": datos["ruta"], "tipo": "concepto", "titulo": datos["titulo"], "alias": datos["aliases"]})
    for c, otros in junto.items():
        for t, n in otros.items():
            if c < t:
                aristas.append({"origen": conceptos[c]["ruta"], "destino": conceptos[t]["ruta"], "tipo": "co_ocurre", "peso": n})
    (raiz / "grafo.json").write_text(
        json.dumps({"nodos": nodos, "aristas": aristas}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


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
    """Secciones H2 de una lección con su ancla y su texto normalizado (sin código ni bloques automáticos)."""
    cuerpo = prosa(texto)
    usados, cabeceras, salida = Counter(), list(re.finditer(r"^(#{1,6})\s+(.+)$", cuerpo, re.M)), []
    for i, m in enumerate(cabeceras):
        titulo = _texto_plano(m.group(2))
        base = slug_ancla(titulo)
        ancla = base if usados[base] == 0 else f"{base}-{usados[base]}"
        usados[base] += 1
        if len(m.group(1)) != 2:
            continue
        fin = cabeceras[i + 1].start() if i + 1 < len(cabeceras) else len(cuerpo)
        bloque = re.sub(r"```.*?```", "", cuerpo[m.start():fin], flags=re.S)
        salida.append({"titulo": titulo, "ancla": ancla, "texto": _norm(_texto_plano(bloque))})
    return salida


def _puntos(texto_norm, aliases):
    total = 0
    for a in aliases:
        alias = _norm(a).strip()
        if len(alias) >= 2:
            total += len(re.findall(rf"(?<![a-z0-9]){re.escape(alias)}(?![a-z0-9])", texto_norm))
    return total


def _celda(t):
    return str(t).replace("|", "/").strip()


def generar_cerebro(raiz, AREAS, conceptos, docs, grupos, menciones):
    """Escribe cerebro/inicio.md: un solo archivo con tablas de acceso rápido, conceptos y lecciones.
    Sustituye al glosario y a los mapas por área, que se borran."""
    carpeta = raiz / "cerebro"
    carpeta.mkdir(exist_ok=True)
    for viejo in carpeta.glob("*.md"):
        viejo.unlink()
    origen = "cerebro/inicio.md"

    secciones = {}
    for area in AREAS:
        for l in grupos[area]:
            secciones[l] = _secciones(docs[l]["texto"])

    # Por cada concepto, las tres secciones de lección donde más aparece.
    donde = {}
    for c, datos in conceptos.items():
        candidatos = []
        for l, lista in secciones.items():
            for orden_sec, sec in enumerate(lista):
                if re.match(r"(glosario|resumen|referencias|conclusi)", _norm(sec["titulo"])):
                    continue  # los resúmenes repiten definiciones: no sirven para ubicar la explicación
                p = _puntos(sec["texto"], datos["aliases"])
                if p:
                    candidatos.append((-p, l, orden_sec, sec))
        candidatos.sort(key=lambda x: (x[0], x[1], x[2]))
        donde[c] = candidatos[:2]

    L = [
        "# Inicio: mapa rápido de los apuntes", "",
        "Índice para buscar con Ctrl+F: escribe el concepto o la sección, en español o en inglés, y sigue el enlace. "
        "Se genera solo con `actualizar`; no lo edites a mano.", "",
        "## Acceso rápido", "",
        "| Quiero... | Ir a | Resultado |", "| --- | --- | --- |",
        f"| Empezar a estudiar | [Bases de datos]({rel_a(origen, 'bases-de-datos/indice.md')}) | Ruta en orden. |",
        "| Buscar un concepto | [Conceptos](#conceptos) | Definición y dónde se enseña. |",
        "| Ver las secciones de una lección | [Lecciones](#lecciones) | Índice de cada lección con sus secciones. |",
        f"| Consultar con Gemini | [Tutorial de Gemini]({rel_a(origen, 'consultar-con-gemini.md')}) | Cómo usar este archivo con Gemini. |",
        f"| Consultar sin conexión | [Tutorial de Ollama]({rel_a(origen, 'tutorial-ollama.md')}) | Modelo local, como último recurso. |",
        f"| Añadir o mantener contenido | [Guía de mantenimiento]({rel_a(origen, 'MANTENIMIENTO.md')}) | Comandos y convenciones. |",
        "",
        "## Conceptos", "",
        "| Concepto | Qué es | También se busca como | Dónde se enseña |", "| --- | --- | --- | --- |",
    ]
    for c in sorted(conceptos, key=lambda c: conceptos[c]["titulo"].lower()):
        datos = conceptos[c]
        resumen = resumen_de(docs[datos["ruta"]]["texto"], max_chars=160)
        qué = _celda(resumen)
        enlaces = " · ".join(
            f"[{AREAS[docs[l]['fm']['area']]['nombre']} {int(docs[l]['fm']['orden']):02d} · {_celda(sec['titulo'])}]"
            f"({rel_a(origen, l)}#{sec['ancla']})"
            for _, l, _, sec in donde[c]
        )
        sinonimos = ", ".join(_celda(x) for x in datos["aliases"] if x != datos["titulo"]) or "—"
        L.append(f"| [{_celda(datos['titulo'])}]({rel_a(origen, datos['ruta'])}) | {qué} | {sinonimos} | {enlaces or '—'} |")

    L += ["", "## Lecciones", ""]
    for area, datos in AREAS.items():
        if not grupos[area]:
            continue
        L += [f"### {datos['nombre']}", "",
              f"Índice: [{datos['nombre']}]({rel_a(origen, datos['indice'])})", ""]
        for i, l in enumerate(grupos[area], 1):
            L.append(f"#### {i:02d} · [{docs[l]['fm']['titulo']}]({rel_a(origen, l)})")
            for sec in secciones[l]:
                L.append(f"- [{sec['titulo']}]({rel_a(origen, l)}#{sec['ancla']})")
            L.append("")

    cabecera = '---\ntitulo: "Inicio: mapa rápido de los apuntes"\ntags: ["cerebro"]\n---\n\n'
    (carpeta / "inicio.md").write_text(cabecera + "\n".join(L).rstrip() + "\n", encoding="utf-8")


# ------------------------------------------------------------------ validar

def validar(raiz=RAIZ):
    errores, avisos = [], []
    AREAS = areas(raiz)
    conceptos = cargar_conceptos(raiz)
    patron, buscar = compilar_terminos(conceptos)
    rels = documentos(raiz)
    existentes = {p.relative_to(raiz).as_posix() for p in raiz.rglob("*") if p.is_file()}
    textos = {r: (raiz / r).read_text(encoding="utf-8") for r in rels}
    anclas = {r: anclas_de(textos[r]) for r in rels}
    menciones_doc = {r: contar_menciones(cuerpo_visible(textos[r]), patron, buscar) for r in rels}
    enlazados = Counter()

    # Toda carpeta de contenido debe ser un área declarada.
    for carpeta in {p.parent.name for p in raiz.glob("*/*.md")} - CARPETAS_ESPECIALES:
        if carpeta not in AREAS:
            errores.append(f"{carpeta}/: carpeta de contenido sin indice.md válido (necesita 'area' y 'area_orden')")

    for r in rels:
        texto = textos[r]
        fm, _ = leer_frontmatter(texto)
        cuerpo = sin_bloques(texto)

        if "titulo" not in fm:
            errores.append(f"{r}: falta 'titulo' en el frontmatter")
        if "orden" in fm:
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
            if objetivo.startswith("conceptos/"):
                enlazados[Path(objetivo).stem] += 1

    for slug, c in conceptos.items():
        otros = sum(1 for r in rels if r != c["ruta"] and slug in menciones_doc[r])
        if otros == 0 and enlazados[slug] == 0:
            avisos.append(f"concepto sin uso en otras notas: {c['ruta']}")

    grandes = []
    for r in rels:
        tokens = len(textos[r]) // 4
        fm_r, _ = leer_frontmatter(textos[r])
        if r.startswith("cerebro/") and tokens > 8000:
            avisos.append(f"{r}: ~{tokens} tokens; es grande para un modelo local, pero sirve para Gemini")
        if "orden" in fm_r and tokens > 6000:
            grandes.append(r)
    if grandes:
        avisos.append(f"{len(grandes)} lecciones superan ~6000 tokens. En el chat usa 'Current selection' "
                      f"sobre la sección que necesites, no la nota completa.")

    for a in avisos:
        print("AVISO   ", a)
    for e in errores:
        print("ERROR   ", e)
    print(f"\n{len(rels)} documentos, {len(conceptos)} conceptos, {len(AREAS)} áreas. "
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


def crear_concepto(raiz, slug, titulo, aliases):
    _slug_valido(slug)
    ruta = raiz / "conceptos" / f"{slug}.md"
    if ruta.exists():
        raise ValueError(f"ya existe conceptos/{slug}.md.")
    lista = list(dict.fromkeys([titulo] + [a.strip() for a in aliases if a.strip()]))
    datos = {"titulo": titulo, "aliases": lista, "tags": ["concepto"]}
    ruta.write_text(fm_texto(datos) + f"# {titulo}\n\n{PENDIENTE} escribe la definición en una o dos frases.\n", encoding="utf-8")
    return ruta


# ------------------------------------------------------------------ CLI

def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    cmd, args = argv[1], argv[2:]
    try:
        if cmd == "actualizar":
            n = enlazar()
            print(f"Enlaces de concepto añadidos: {n}")
            regenerar()
            print("Índices, mapas, cerebro y grafo.json regenerados.")
            return validar()
        if cmd == "enlazar":
            print(f"Enlaces de concepto añadidos: {enlazar()}")
            return 0
        if cmd == "regenerar":
            regenerar()
            print("Índices, mapas, cerebro y grafo.json regenerados.")
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
        if cmd == "nuevo-concepto" and len(args) in (2, 3):
            aliases = args[2].split("|") if len(args) == 3 else []
            print("Creado:", crear_concepto(RAIZ, args[0], args[1], aliases).relative_to(RAIZ).as_posix())
            print("Siguiente paso: escribe la definición, luego ejecuta 'actualizar'.")
            return 0
    except ValueError as e:
        print("ERROR   ", e)
        return 2
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
