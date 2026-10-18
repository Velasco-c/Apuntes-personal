---
titulo: "Modelo lógico relacional"
aliases: ["Modelo lógico relacional", "modelo lógico relacional", "modelo relacional"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Modelo lógico relacional

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

El **modelo lógico relacional** es la etapa de diseño en la que el [MER](mer.md) se transforma en un conjunto de tablas, columnas, claves y restricciones. Todavía es independiente del motor concreto que se usará.

## Reglas generales de transformación

* Cada entidad se convierte en una tabla.
* Cada atributo simple se convierte en una columna.
* Cada tabla define una [llave primaria](../estructura/llave-primaria.md).
* Una relación 1:N se implementa con una [llave foránea](../estructura/llave-foranea.md) en la tabla del lado "muchos".
* Una relación N:M se implementa con una tabla intermedia.
* Un atributo multivaluado se convierte en una tabla propia.

## Resultado

El esquema resultante se traduce al lenguaje de un [SGBD](../sgbd.md) concreto mediante sentencias de [SQL](../../sql/sql.md), como `CREATE TABLE`. Después se revisa con la [normalización](normalizacion.md) para eliminar la redundancia.

## Ver también

* [Modelo entidad-relación (MER)](mer.md): la etapa anterior.
* [Normalización](normalizacion.md): la revisión que se aplica sobre este modelo.
