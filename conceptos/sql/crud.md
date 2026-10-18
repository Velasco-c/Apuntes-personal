---
titulo: "CRUD"
aliases: ["CRUD", "operaciones CRUD"]
categoria: "sql"
tags: ["concepto"]
---

# CRUD

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

**CRUD** es el acrónimo de *Create, Read, Update, Delete*: las cuatro operaciones básicas que se realizan sobre cualquier dato almacenado.

| Operación | Sentencia SQL | Qué hace |
| --- | --- | --- |
| Create | `INSERT` | Crea registros |
| Read | `SELECT` | Consulta registros |
| Update | `UPDATE` | Modifica registros |
| Delete | `DELETE` | Elimina registros |

## Fuera de las bases de datos

El concepto también describe las rutas de una API REST. Por ejemplo, `POST /productos` crea un producto, `GET /productos/:id` lo lee, `PUT /productos/:id` lo actualiza y `DELETE /productos/:id` lo elimina.

## Errores frecuentes

Un error común es implementar `DELETE` como una eliminación física cuando el sistema necesita conservar el historial. Una alternativa es el borrado lógico: una columna como `activo` pasa a `0`, y las consultas normales filtran los registros inactivos. Otra precaución es validar los datos antes del `INSERT` y del `UPDATE`, porque CRUD no decide por sí solo si un cambio es correcto.

## Ver también

* [SQL](sql.md): el lenguaje que implementa las operaciones.
* [Endpoint](../web/endpoint.md): donde las operaciones CRUD se exponen en una API.
