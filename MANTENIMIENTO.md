---
titulo: "Guía de mantenimiento"
tags: ["mantenimiento"]
---

# Guía de mantenimiento

Cómo añadir contenido y mantener los apuntes ordenados. Sirve para una persona y para una IA que ayude a editar el repositorio.

## El script

`herramientas/mantenimiento.py` es un programa en Python 3 que se ejecuta desde la raíz del repositorio. No es una nota: Obsidian no lo muestra y no hace falta para leer los apuntes. Hace tres cosas: crea archivos nuevos con su estructura, regenera los bloques automáticos (índices, categorías, mapa, cerebro y grafo) y valida el repositorio.

Después de cualquier cambio, ejecuta:

```bash
python3 herramientas/mantenimiento.py actualizar
```

Si la validación encuentra un error, el mensaje indica el archivo y el problema. Los avisos no detienen la validación, pero conviene revisarlos.

## Añadir contenido

Un área nueva de lecciones. El número define su lugar en el README, el mapa y el cerebro:

```bash
python3 herramientas/mantenimiento.py nueva-area express "Express" 6
```

Una lección dentro de un área. El número define el orden:

```bash
python3 herramientas/mantenimiento.py nueva-leccion express 1 introduccion "Introducción a Express"
```

Una categoría de conceptos. Si es una subcategoría, la categoría padre debe existir antes:

```bash
python3 herramientas/mantenimiento.py nueva-categoria bases-de-datos/transacciones "Transacciones" 3
```

Un concepto. Los alias son las formas en que aparece el término, separadas por `|`, y el último argumento es la categoría, es decir, la ruta de su carpeta:

```bash
python3 herramientas/mantenimiento.py nuevo-concepto middleware "Middleware" "middleware|middlewares" web
```

Cada archivo nuevo trae una línea `PENDIENTE:`. Reemplázala por el contenido real y ejecuta `actualizar`. Mientras quede alguna, la validación falla.

## Cómo está organizado el contenido

### Lecciones

Cada área es una carpeta con su `indice.md`. Las lecciones se llaman `NN-nombre.md` y tienen el frontmatter `titulo`, `area`, `orden` y `tags`. Si una lección supera unos 6000 tokens, conviene dividirla.

### Conceptos

Los conceptos están en carpetas por categoría, por ejemplo `conceptos/bases-de-datos/modelado/`. Cada carpeta contiene un `categoria.md` con su nombre, su orden y una descripción del tema que reúne.

Un concepto general no lleva el nombre de una tecnología. DTO, por ejemplo, es un patrón que puede usarse con Express, pero no es parte de Express. Las tecnologías concretas, como MySQL, PostgreSQL o Express, tienen su propia nota que se apoya en los conceptos generales. Si un término solo tiene sentido dentro de una lección, va en la lección y no en `conceptos/`.

## Cómo escribir un concepto

Un concepto debe explicar el tema, no solo enlazar otras notas. La estructura es la siguiente:

1. Frontmatter con `titulo`, `aliases`, `categoria` (debe coincidir con su carpeta) y `tags`.
2. El título (`#`). La línea de categoría que aparece debajo se genera sola.
3. Un primer párrafo que dice qué es, en una o dos frases, con el término en **negrita**. El cerebro toma ese párrafo como resumen.
4. El desarrollo en secciones `##`: cómo funciona, un ejemplo, errores comunes o cuándo usarlo. Debe tener al menos unas 120 palabras; el validador avisa si tiene menos.
5. `## Ver también`, con dos o tres enlaces y el motivo de cada uno. Solo se enlazan conceptos realmente relacionados.

Los bloques de código indican su lenguaje. Los ejemplos deben ser cortos y comprobables.

## Enlaces

* Los enlaces entre conceptos se escriben a mano. El script no los inserta automáticamente.
* Usa Markdown relativo, como `[Tabla](../estructura/tabla.md)`. No uses `[[wikilinks]]`.
* Enlaza la primera mención importante de un concepto dentro de una lección, no cada aparición del término.

## Convenciones

* Carpetas en minúsculas y con guiones.
* Índices de área: `indice.md` con `nombre` y `area_orden`.
* Categorías: `categoria.md` con `titulo`, `categoria`, `nombre`, `orden` y `tags`.
* Encabezados: un solo `#` por archivo. Las secciones son `##` y las subsecciones `###`, sin saltar niveles.
* Diagramas: bloques `mermaid`, no imágenes.
* Ejercicios: son contenido aprobado. Corrige enlaces y encabezados, pero no reescribas su texto.

## Lo que se genera solo

No edites nada que esté entre `<!-- auto:... -->` y `<!-- /auto:... -->`. Se regenera en cada `actualizar`:

* El pie de cada lección, con la navegación entre lecciones.
* La línea de categoría de cada concepto.
* El índice de cada área (sus lecciones) y el de cada categoría (sus conceptos, con su resumen).
* La lista de áreas y de categorías del README, y el mapa de contenidos.
* `cerebro/inicio.md`: los conceptos agrupados por categoría, con su definición.
* `cerebro/lecciones.md`: las secciones de cada lección.
* `grafo.json`: la red completa en formato de datos.

## Validación

Los **errores** detienen la validación: enlaces rotos, encabezados mal anidados, conceptos en una carpeta distinta a su `categoria`, alias repetidos en dos conceptos y líneas `PENDIENTE:` sin completar.

Los **avisos** no la detienen, pero conviene revisarlos: conceptos con menos de 120 palabras, conceptos sin secciones, conceptos que ninguna otra nota enlaza y archivos grandes.

## Límites

* Una lección de más de unos 6000 tokens es grande para un chat local. Consúltala con *Current selection*.
* Si `cerebro/lecciones.md` supera unos 8000 tokens, el validador avisa. Para Gemini no supone problema.
