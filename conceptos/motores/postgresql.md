---
titulo: "PostgreSQL"
aliases: ["PostgreSQL", "Postgres"]
categoria: "motores"
tags: ["concepto"]
---

# PostgreSQL

<!-- auto:categoria -->
Categoría: [Motores de base de datos](categoria.md)
<!-- /auto:categoria -->

**PostgreSQL** es un sistema gestor de bases de datos relacionales de código abierto. Destaca por su cumplimiento del estándar [SQL](../sql/sql.md), su extensibilidad y su soporte para tipos de datos avanzados, como [JSON](../formatos/json.md) y los arreglos.

## Características

* Tipos avanzados: JSON y JSONB, arreglos, rangos y datos geométricos.
* Funciones de ventana, CTE y vistas materializadas.
* Extensiones que añaden funcionalidades, como la programación de tareas.

## Diferencias frecuentes con MySQL

PostgreSQL tiene un tipo booleano nativo, mientras que MySQL lo representa como `TINYINT(1)`. Para generar identificadores, MySQL usa `AUTO_INCREMENT`, y PostgreSQL usa `SERIAL` o columnas de identidad. Ambos son relacionales y comparten los conceptos generales.

## Ver también

* [MySQL](mysql.md): el otro motor relacional de esta base de conocimientos.
* [Sistema gestor de bases de datos (SGBD)](../bases-de-datos/sgbd.md): la categoría general a la que pertenece.
