---
titulo: "Llave (clave)"
aliases: ["Llave (clave)", "llave", "llaves"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Llave (clave)

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **llave**, también llamada **clave**, es un atributo o conjunto de atributos que identifica o relaciona filas dentro de una base de datos. Las llaves son el mecanismo de integridad que permite distinguir un registro de los demás y expresar las relaciones entre tablas.

## Tipos de llave

* **Superllave:** cualquier conjunto de atributos que identifica una fila de forma única.
* **Llave candidata:** una superllave mínima. Si se quita cualquiera de sus atributos, deja de identificar filas de forma única.
* **[Llave primaria](llave-primaria.md):** la llave candidata que se elige para identificar las filas de la tabla.
* **[Llave foránea](llave-foranea.md):** un atributo que referencia la llave primaria de otra tabla.

## Ejemplo

En una tabla de estudiantes, `codigo` puede ser una llave candidata si no se repite. Si se elige como llave primaria, el motor impide que se inserten dos filas con el mismo código.

## Ver también

* [Llave primaria (PK)](llave-primaria.md): la llave que identifica cada fila.
* [Llave foránea (FK)](llave-foranea.md): la llave que relaciona tablas.
