---
titulo: "JOIN"
aliases: ["JOIN", "joins"]
categoria: "sql"
tags: ["concepto"]
---

# JOIN

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Un **JOIN** es una operación SQL que combina filas de dos o más tablas según una condición. La condición suele comparar una [llave foránea](../bases-de-datos/estructura/llave-foranea.md) con la llave primaria a la que hace referencia.

## Tipos principales

* **INNER JOIN:** devuelve solo las filas que cumplen la condición en ambas tablas.
* **LEFT JOIN:** devuelve todas las filas de la tabla izquierda, con `NULL` donde no hay coincidencia a la derecha.
* **RIGHT JOIN:** es el inverso de LEFT JOIN.
* **FULL JOIN:** devuelve todas las filas de ambas tablas. MySQL no lo implementa de forma directa.

## Ejemplo

```sql
SELECT c.nombre, p.id AS pedido
FROM clientes AS c
INNER JOIN pedidos AS p ON p.cliente_id = c.id;
```

## Ver también

* [Llave foránea (FK)](../bases-de-datos/estructura/llave-foranea.md): la condición habitual de un JOIN.
* [SQL](sql.md): el lenguaje en el que se escribe.
