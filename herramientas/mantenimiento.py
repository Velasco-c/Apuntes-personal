#!/usr/bin/env python3
"""Mantenimiento de la colección de apuntes.

Uso, desde la raíz del repositorio:

  python3 herramientas/mantenimiento.py regenerar
      Actualiza los bloques automáticos (navegación, conceptos de cada lección,
      dónde aparece cada concepto, índices y mapa) y escribe grafo.json.

  python3 herramientas/mantenimiento.py validar
      Revisa enlaces, encabezados, frontmatter, nombres de archivo y conceptos
      sin uso. Devuelve código de salida 1 si encuentra errores.

Los bloques delimitados por <!-- auto:nombre --> se generan solos: no los edites a mano.
"""
import json
import posixpath
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parent.parent

AREAS = {
    "bases-de-datos": "Bases de datos",
    "mysql": "MySQL",
    "postgresql": "PostgreSQL",
    "nodejs": "Node.js",
    "inteligencia-artificial": "Inteligencia artificial",
}
ARCHIVOS_RAIZ = {"README.md", "MAPA.md", "MANTENIMIENTO.md"}

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
BLOQUE_AUTO_RE = re.compile(r"\n*<!-- auto:(\w+) -->.*?<!-- /auto:\1 -->\n*", re.S)
ENLACE_RE = re.compile(r"(!?)\[([^\]\n]*)\]\(((?:[^()\s]|\([^()\s]*\))+)\)")


# ---------------------------------------------------------------- utilidades

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


def documentos(raiz):
    """Rutas relativas (posix) de todos los .md, excluyendo herramientas y ocultos."""
    salida = []
    for p in sorted(raiz.rglob("*.md")):
        rel = p.relative_to(raiz).as_posix()
        if rel.startswith("herramientas/") or "/." in rel or rel.startswith("."):
            continue
        salida.append(rel)
    return salida


def sin_bloques(texto):
    """Cuerpo sin frontmatter ni bloques de código delimitados (conserva el código en línea, útil para encabezados)."""
    _, cuerpo = leer_frontmatter(texto)
    return re.sub(r"```.*?```", "", cuerpo, flags=re.S)


def sin_codigo(texto):
    """Cuerpo sin frontmatter, bloques de código ni código en línea."""
    _, cuerpo = leer_frontmatter(texto)
    cuerpo = re.sub(r"```.*?```", "", cuerpo, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", cuerpo)


def cuerpo_visible(texto):
    """Solo prosa: sin frontmatter, bloques automáticos, código, comentarios ni destinos de enlaces."""
    _, cuerpo = leer_frontmatter(texto)
    cuerpo = BLOQUE_AUTO_RE.sub("\n", cuerpo)
    cuerpo = re.sub(r"<!--.*?-->", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"```.*?```", "", cuerpo, flags=re.S)
    cuerpo = re.sub(r"`[^`\n]*`", "", cuerpo)
    cuerpo = re.sub(r"\]\([^)\n]*\)", "]", cuerpo)
    return cuerpo


def rel_a(desde, hacia):
    """Ruta relativa de 'hacia' vista desde el archivo 'desde' (ambas relativas a la raíz)."""
    return posixpath.relpath(hacia, posixpath.dirname(desde) or ".")


def poner_bloque(texto, nombre, contenido):
    """Reemplaza (o añade al final) el bloque automático con ese nombre."""
    patron = re.compile(rf"\n*<!-- auto:{nombre} -->.*?<!-- /auto:{nombre} -->\n*", re.S)
    base = patron.sub("\n", texto).rstrip() + "\n"
    return base + f"\n<!-- auto:{nombre} -->\n{contenido.strip()}\n<!-- /auto:{nombre} -->\n"


def slug_ancla(texto):
    """Convierte un encabezado en ancla, con la misma lógica básica que GitHub."""
    texto = re.sub(r"[`*_]", "", texto.strip().lower())
    texto = re.sub(r"[^\w\- ]", "", texto)
    return texto.replace(" ", "-")


# ---------------------------------------------------------------- conceptos y términos

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
    """Patrón único para todos los términos. Los alias más largos ganan (p. ej. 'llaves foráneas' sobre 'llaves').
    Las siglas (todo en mayúsculas) se buscan sensibles a mayúsculas; el resto, sin distinguir."""
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


# ---------------------------------------------------------------- regenerar

def regenerar(raiz=RAIZ):
    conceptos = cargar_conceptos(raiz)
    patron, buscar = compilar_terminos(conceptos)

    docs = {}
    for rel in documentos(raiz):
        texto = (raiz / rel).read_text(encoding="utf-8")
        docs[rel] = {"texto": texto, "fm": leer_frontmatter(texto)[0]}

    def titulo(r):
        return docs[r]["fm"]["titulo"]

    # Lecciones: tienen 'orden'. Se ordenan por área (orden de AREAS) y luego por 'orden'.
    lecciones = sorted(
        (r for r in docs if "orden" in docs[r]["fm"]),
        key=lambda r: (list(AREAS).index(docs[r]["fm"]["area"]), int(docs[r]["fm"]["orden"])),
    )
    grupos = defaultdict(list)
    for r in lecciones:
        grupos[docs[r]["fm"]["area"]].append(r)
    menciones = {r: contar_menciones(cuerpo_visible(docs[r]["texto"]), patron, buscar) for r in lecciones}

    # 1. Pie de cada lección: navegación y conceptos.
    for r in lecciones:
        area = docs[r]["fm"]["area"]
        g = grupos[area]
        k = g.index(r)
        nav = []
        if k > 0:
            nav.append(f"[← Anterior: {titulo(g[k - 1])}]({rel_a(r, g[k - 1])})")
        nav.append(f"[Índice de {AREAS[area]}]({rel_a(r, area + '/indice.md')})")
        if k < len(g) - 1:
            nav.append(f"[Siguiente: {titulo(g[k + 1])} →]({rel_a(r, g[k + 1])})")
        top = [s for s, _ in menciones[r].most_common(15)]
        conc = ", ".join(f"[{conceptos[s]['titulo']}]({rel_a(r, conceptos[s]['ruta'])})" for s in top)
        contenido = (
            "---\n\n**Navegación:** " + " · ".join(nav)
            + "\n\n**Conceptos de esta lección:** " + (conc or "ninguno")
        )
        docs[r]["texto"] = poner_bloque(docs[r]["texto"], "pie", contenido)

    # 2. Cada concepto: dónde aparece y qué conceptos le acompañan.
    donde = defaultdict(list)
    junto = defaultdict(Counter)
    for r in lecciones:
        m = menciones[r]
        for s, n in m.items():
            donde[s].append((r, n))
            junto[s].update(t for t in m if t != s)
    for s, c in conceptos.items():
        r = c["ruta"]
        items = sorted(donde[s], key=lambda x: (-x[1], titulo(x[0])))
        if items:
            lista = "\n".join(
                f"- [{titulo(l)}]({rel_a(r, l)}) · {AREAS[docs[l]['fm']['area']]} · "
                f"{n} {'mención' if n == 1 else 'menciones'}"
                for l, n in items
            )
        else:
            lista = "Todavía no aparece en ninguna lección."
        vecinos = [t for t, _ in junto[s].most_common(8)]
        cerca = ", ".join(f"[{conceptos[t]['titulo']}]({rel_a(r, conceptos[t]['ruta'])})" for t in vecinos)
        contenido = f"## Dónde aparece\n\n{lista}\n\n## Conceptos cercanos\n\n{cerca or 'Ninguno todavía.'}"
        docs[r]["texto"] = poner_bloque(docs[r]["texto"], "backlinks", contenido)

    # 3. Índices de área.
    for area in AREAS:
        ruta = f"{area}/indice.md"
        if ruta in docs:
            lista = "\n".join(f"{i}. [{titulo(l)}]({rel_a(ruta, l)})" for i, l in enumerate(grupos[area], 1))
            docs[ruta]["texto"] = poner_bloque(docs[ruta]["texto"], "lecciones", "## Lecciones\n\n" + lista)

    # 4. Mapa de contenidos.
    if "MAPA.md" in docs:
        partes = []
        for area, nombre in AREAS.items():
            if grupos[area]:
                items = "\n".join(f"{i}. [{titulo(l)}]({rel_a('MAPA.md', l)})" for i, l in enumerate(grupos[area], 1))
                partes.append(f"## {nombre}\n\n{items}")
        conc = "\n".join(
            f"- [{c['titulo']}]({rel_a('MAPA.md', c['ruta'])})"
            for c in sorted(conceptos.values(), key=lambda c: c["titulo"].lower())
        )
        partes.append(f"## Conceptos\n\n{conc}")
        docs["MAPA.md"]["texto"] = poner_bloque(docs["MAPA.md"]["texto"], "mapa", "\n\n".join(partes))

    # 5. Grafo para máquinas (y para exploradores de la red).
    nodos, aristas = [], []
    for r in lecciones:
        fm = docs[r]["fm"]
        nodos.append({"id": r, "tipo": "leccion", "titulo": fm["titulo"], "area": fm["area"], "orden": int(fm["orden"])})
        for s, n in menciones[r].items():
            aristas.append({"origen": r, "destino": conceptos[s]["ruta"], "tipo": "menciona", "peso": n})
    for a, b in zip(lecciones, lecciones[1:]):
        if docs[a]["fm"]["area"] == docs[b]["fm"]["area"]:
            aristas.append({"origen": a, "destino": b, "tipo": "sigue_a", "peso": 1})
    for s, c in conceptos.items():
        nodos.append({"id": c["ruta"], "tipo": "concepto", "titulo": c["titulo"], "alias": c["aliases"]})
    for s, otros in junto.items():
        for t, n in otros.items():
            if s < t:
                aristas.append({"origen": conceptos[s]["ruta"], "destino": conceptos[t]["ruta"], "tipo": "co_ocurre", "peso": n})
    (raiz / "grafo.json").write_text(
        json.dumps({"nodos": nodos, "aristas": aristas}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )

    for rel, d in docs.items():
        (raiz / rel).write_text(d["texto"], encoding="utf-8")


# ---------------------------------------------------------------- validar

def validar(raiz=RAIZ):
    errores, avisos = [], []
    conceptos = cargar_conceptos(raiz)
    patron, buscar = compilar_terminos(conceptos)
    rels = documentos(raiz)
    existentes = {p.relative_to(raiz).as_posix() for p in raiz.rglob("*") if p.is_file()}
    textos = {r: (raiz / r).read_text(encoding="utf-8") for r in rels}
    anclas = {r: {slug_ancla(t) for t in re.findall(r"^#{1,6}\s+(.+)$", sin_bloques(textos[r]), re.M)} for r in rels}
    menciones_por_doc = {r: contar_menciones(cuerpo_visible(textos[r]), patron, buscar) for r in rels}
    enlazados = Counter()

    for r in rels:
        texto = textos[r]
        fm, _ = leer_frontmatter(texto)
        cuerpo = sin_codigo(texto)

        if "titulo" not in fm:
            errores.append(f"{r}: falta 'titulo' en el frontmatter")
        if "orden" in fm and not r.startswith(fm.get("area", "?") + "/"):
            errores.append(f"{r}: la lección no está en la carpeta de su área '{fm.get('area')}'")

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
        if nombre not in ARCHIVOS_RAIZ and not re.fullmatch(r"(\d{2}-)?[a-z0-9]+(-[a-z0-9]+)*\.md", nombre):
            errores.append(f"{r}: nombre de archivo no válido (usa minúsculas, guiones y sin espacios)")
        if "[[" in cuerpo:
            errores.append(f"{r}: contiene wikilinks [[...]]; usa enlaces Markdown")

        for m in ENLACE_RE.finditer(cuerpo):
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
        otros = sum(1 for r in rels if r != c["ruta"] and slug in menciones_por_doc[r])
        if otros == 0 and enlazados[slug] == 0:
            avisos.append(f"concepto sin uso en otras notas: {c['ruta']}")

    for a in avisos:
        print("AVISO   ", a)
    for e in errores:
        print("ERROR   ", e)
    print(f"\n{len(rels)} documentos, {len(conceptos)} conceptos. Errores: {len(errores)}. Avisos: {len(avisos)}.")
    return 1 if errores else 0


# ---------------------------------------------------------------- CLI

def main(argv):
    if len(argv) != 2 or argv[1] not in ("regenerar", "validar"):
        print(__doc__)
        return 2
    if argv[1] == "regenerar":
        regenerar()
        print("Bloques automáticos, índices, mapa y grafo.json regenerados.")
        return 0
    return validar()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
