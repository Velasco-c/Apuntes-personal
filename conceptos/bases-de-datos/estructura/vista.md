---
titulo: "Vista"
aliases: ["Vista", "vista", "vistas", "view"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Vista

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **vista** es una consulta guardada con un nombre, que se usa como si fuera una tabla. Normalmente no almacena datos propios: cada vez que se consulta, el motor ejecuta de nuevo la consulta sobre las tablas base.

## Para qué sirve

* Ocultar columnas sensibles a ciertos usuarios.
* Simplificar consultas largas que se repiten.
* Presentar los datos en la forma que necesita una aplicación, sin cambiar las tablas.

## Ejemplo

```sql
CREATE VIEW productos_activos AS
SELECT id, nombre, precio
FROM productos
WHERE activo = 1;

SELECT * FROM productos_activos;
```

## Vistas materializadas

Algunos motores permiten guardar el resultado de la consulta para no recalcularlo cada vez. PostgreSQL las llama vistas materializadas. MySQL no las ofrece de forma nativa.

## Limitaciones

No todas las vistas pueden modificarse con `INSERT`, `UPDATE` o `DELETE`. Como regla general, las vistas que combinan varias tablas o usan agregaciones son de solo lectura. MySQL permite `WITH CHECK OPTION`, que impide insertar o modificar filas que la vista no mostraría después.

Una vista no mejora el rendimiento por sí misma: el motor ejecuta la consulta completa cada vez que se consulta la vista.

## Ver también

* [Tabla](tabla.md): la fuente de datos de la vista.
* [SQL](../../sql/sql.md): el lenguaje en el que se define la consulta.
