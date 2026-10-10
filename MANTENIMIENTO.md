---
titulo: "Guía de mantenimiento"
tags: ["mantenimiento"]
---

# Guía de mantenimiento

Convenciones para mantener la colección ordenada y conectada. Sirven tanto para una persona como para una IA que ayude a editar el repositorio.

## Estructura de carpetas

- Un tema es una carpeta. Cada carpeta de área tiene su `indice.md`.
- Las lecciones empiezan con dos dígitos de orden: `01-nombre.md`.
- `conceptos/` es plana: todas las notas de concepto van ahí, sin subcarpetas.
- Los nombres de archivo van en minúsculas, con guiones, sin acentos ni espacios.

## Frontmatter

Toda nota empieza con un bloque YAML:

- Lecciones: `titulo`, `area`, `orden` y `tags`.
- Conceptos: `titulo`, `aliases` (las formas en que el concepto aparece en el texto: singular, plural, siglas) y `tags: ["concepto"]`.
- Índices y mapa: `titulo` y `area` o `tags`.

## Encabezados

Un solo `#` por archivo, que es el título. Las secciones usan `##` y las subsecciones `###`. No saltes niveles.

## Enlaces

Usa rutas relativas en Markdown, por ejemplo `[Transacción](../conceptos/transaccion.md)`. No uses `[[wikilinks]]`, porque GitHub no los muestra. Enlaza un concepto la primera vez que aparece en una lección, como ya se hace en las clases de bases de datos.

## Agregar un concepto

1. Crea `conceptos/nombre.md` con su frontmatter y una definición breve.
2. Escribe en `aliases` las formas en que aparece en el texto.
3. Ejecuta `python3 herramientas/mantenimiento.py regenerar`.

## Bloques automáticos

Todo lo que está entre `<!-- auto:... -->` se genera solo: la navegación y los conceptos de cada lección, el apartado "Dónde aparece" de cada concepto, los índices y el mapa. No lo edites a mano, porque se sobrescribe.

## Contenido aprobado

Los ejercicios de las lecciones se consideran contenido aprobado. Al revisar, corrige enlaces y encabezados, pero no reescribas su enunciado ni su solución sin que el autor lo pida.

## Comprobar el repositorio

```
python3 herramientas/mantenimiento.py validar
```

Revisa enlaces rotos, saltos de encabezado, frontmatter, nombres de archivo y conceptos sin uso. Devuelve error si algo falla, así que puede usarse antes de cada cambio.
