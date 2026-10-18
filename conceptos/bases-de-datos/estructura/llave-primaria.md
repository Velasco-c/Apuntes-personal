---
titulo: "Llave primaria (PK)"
aliases: ["Llave primaria (PK)", "llave primaria", "clave primaria", "PK"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Llave primaria (PK)

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **llave primaria** (PK, *primary key*) es el atributo o conjunto de atributos que identifica de forma única e inequívoca cada fila de una tabla. Cada tabla tiene una sola llave primaria, y sus columnas no admiten valores `NULL`.

## Características

* Sus valores son únicos: no pueden existir dos filas con la misma llave primaria.
* No admite `NULL`, porque una fila sin identificador no podría localizarse.
* Debe ser estable: conviene que su valor nunca cambie.
* Suele ser un número generado automáticamente.

## Ejemplo en MySQL

```sql
CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);
```

`AUTO_INCREMENT` genera el valor de `id` al insertar cada fila.

## Llave natural o artificial

Una **llave natural** usa un dato que ya existe en el mundo real, como el código de un producto o un correo electrónico. Una **llave artificial** es un identificador que se genera solo para la base de datos, como un número autoincrementable. Las llaves artificiales son más estables, porque el dato natural puede cambiar, por ejemplo cuando un cliente cambia de correo.

## Ver también

* [Llave (clave)](llave.md): la familia de conceptos a la que pertenece.
* [Llave foránea (FK)](llave-foranea.md): la llave que referencia a la primaria de otra tabla.
