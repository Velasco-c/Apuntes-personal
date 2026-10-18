---
titulo: "Tupla"
aliases: ["Tupla", "tupla", "tuplas"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Tupla

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **tupla**, también llamada **fila** o **registro**, es una ocurrencia única de una entidad dentro de una tabla. Cada tupla contiene un valor para cada columna de la tabla.

## Características

* Si la tabla tiene una [llave primaria](llave-primaria.md), dos tuplas no pueden tener el mismo valor en ella.
* El orden de las tuplas no tiene significado en el modelo relacional. El orden se define en la consulta con `ORDER BY`.
* Una tupla puede tener valores `NULL` en las columnas que lo permitan. `NULL` significa ausencia de valor, no cero ni texto vacío.

## Ejemplo

| id | nombre | precio |
| --- | --- | --- |
| 1 | Teclado mecánico | 350.00 |
| 2 | Mouse inalámbrico | 120.50 |

Cada una de estas filas es una tupla de la tabla `productos`.

## Ver también

* [Tabla](tabla.md): la estructura que contiene las tuplas.
* [Llave primaria (PK)](llave-primaria.md): lo que distingue una tupla de las demás.
