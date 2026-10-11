---
titulo: "Guía de mantenimiento"
tags: ["mantenimiento"]
---

# Guía de mantenimiento

Cómo añadir contenido y mantener los apuntes ordenados. Sirve para una persona y para una IA que ayude a editar el repositorio.

## El script

`herramientas/mantenimiento.py` es un programa en Python 3 que se ejecuta en la terminal, desde la raíz del repositorio. No es una nota: Obsidian no lo muestra, y no lo necesitas para leer los apuntes. Hace cuatro cosas: crear archivos nuevos, enlazar conceptos, regenerar los bloques automáticos (incluido `cerebro/inicio.md`) y validar el repositorio. `validar` revisa enlaces y anclas, encabezados, nombres de archivo, frontmatter, líneas `PENDIENTE:` y el tamaño del contexto.

Después de cualquier cambio, ejecuta:

```bash
python3 herramientas/mantenimiento.py actualizar
```

Ese único comando enlaza, regenera y valida. Si la validación falla, el mensaje indica el archivo y el problema.

## Añadir contenido

Un área nueva. El número define su lugar en el README, el mapa y el cerebro:

```bash
python3 herramientas/mantenimiento.py nueva-area express "Express" 6
```

Una lección dentro de un área. El número define el orden:

```bash
python3 herramientas/mantenimiento.py nueva-leccion express 1 introduccion "Introducción a Express"
```

Un concepto. Los alias son las formas en que aparece en el texto, separadas por `|`:

```bash
python3 herramientas/mantenimiento.py nuevo-concepto middleware "Middleware" "middleware|middlewares"
```

Cada archivo nuevo tiene una línea que empieza con `PENDIENTE:`. Reemplázala por el contenido real y ejecuta `actualizar`. Mientras quede alguna, la validación falla, para no publicar contenido incompleto.

## Convenciones

- Una carpeta por tema, en minúsculas y con guiones. `conceptos/` es plana: todos los conceptos van ahí.
- Lecciones: `NN-nombre.md`, con frontmatter `titulo`, `area`, `orden` y `tags`.
- Índices: `indice.md` con `nombre` y `area_orden`. Así el script reconoce el área.
- Conceptos: `titulo` y `aliases`, y una definición breve al principio.
- Encabezados: un solo `#` por archivo. Las secciones son `##` y las subsecciones `###`, sin saltar niveles.
- Enlaces: Markdown relativo, como `[Texto](../conceptos/x.md)`. No uses `[[wikilinks]]`.
- Diagramas: bloques `mermaid`, no imágenes.
- Ejercicios: son contenido aprobado. Corrige enlaces y encabezados, pero no reescribas su texto.

## Lo que se genera solo

No edites nada que esté entre `<!-- auto:... -->`. Se regenera en cada `actualizar`:

- El pie de cada lección, el apartado "Dónde aparece" de cada concepto, los índices, el mapa y la lista de áreas del README.
- `cerebro/inicio.md`: un único archivo con tablas de acceso rápido, los conceptos (con su definición y dónde se enseñan) y las lecciones (con sus secciones). Es el archivo que se sube a Gemini. No hay que escribirlo a mano.
- `grafo.json`: la red completa en formato de datos. Obsidian no lo usa; sirve para herramientas que necesiten leer la estructura.

## Límites

- Una lección de más de unos 6000 tokens es grande para un chat local. Consúltala con *Current selection*.
- Si `cerebro/inicio.md` supera unos 8000 tokens, el validador avisa. Para un modelo local es grande; para Gemini no supone problema.
