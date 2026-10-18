---
titulo: "SQL"
aliases: ["SQL", "lenguaje SQL"]
categoria: "sql"
tags: ["concepto"]
---

# SQL

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

**SQL** (*Structured Query Language*) es el lenguaje estándar para definir, consultar y manipular datos en bases de datos relacionales. Casi todos los motores relacionales lo usan, aunque cada uno implementa variaciones propias.

## Subconjuntos del lenguaje

* **DDL** (definición de datos): `CREATE`, `ALTER` y `DROP` definen estructuras.
* **DML** (manipulación de datos): `INSERT`, `UPDATE`, `DELETE` y `SELECT` cambian o consultan los datos.
* **DCL** (control de datos): `GRANT` y `REVOKE` administran permisos.
* **TCL** (control de transacciones): `COMMIT` y `ROLLBACK` confirman o revierten cambios.

## Ejemplo

```sql
SELECT nombre, precio
FROM productos
WHERE precio < 200
ORDER BY precio;
```

## Dialectos

Los motores extienden el estándar. `AUTO_INCREMENT` es propio de MySQL, mientras que PostgreSQL usa `SERIAL` o columnas de identidad para generar identificadores. Por eso una misma idea puede escribirse de forma distinta según el [motor](../motores/mysql.md).

## Ver también

* [CRUD](crud.md): las cuatro operaciones básicas que se expresan en SQL.
* [Base de datos relacional](../bases-de-datos/base-de-datos-relacional.md): el modelo para el que se diseñó SQL.
