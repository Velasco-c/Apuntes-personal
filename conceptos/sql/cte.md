---
titulo: "CTE"
aliases: ["CTE", "common table expression"]
categoria: "sql"
tags: ["concepto"]
---

# CTE

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Una **CTE** (*Common Table Expression*, expresión de tabla común) es una consulta temporal con nombre, definida con `WITH` al inicio de una sentencia. Se usa como si fuera una tabla dentro de esa sentencia y permite dividir una consulta compleja en pasos legibles.

## Ejemplo

```sql
WITH totales AS (
    SELECT cliente_id, SUM(total) AS gasto
    FROM pedidos
    GROUP BY cliente_id
)
SELECT c.nombre, t.gasto
FROM clientes AS c
INNER JOIN totales AS t ON t.cliente_id = c.id;
```

## CTE recursivas

Una CTE puede referirse a sí misma para recorrer jerarquías, como un organigrama o un árbol de categorías. MySQL las admite desde la versión 8.0.

## Cuándo usar una CTE en lugar de una subconsulta

Una CTE conviene cuando la misma consulta intermedia se usa varias veces dentro de la sentencia, o cuando la subconsulta anidada es difícil de leer. Una subconsulta simple dentro de un `WHERE` puede ser más directa. La elección depende de la claridad: lo que se entiende mejor en el momento de escribirlo suele ser lo que se mantiene mejor después.

## Ver también

* [Función de ventana](funcion-de-ventana.md): a menudo se combinan con CTE para preparar los datos.
* [JOIN](join.md): la forma habitual de combinar la CTE con otras tablas.
