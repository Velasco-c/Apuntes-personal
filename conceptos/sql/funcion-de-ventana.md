---
titulo: "Función de ventana"
aliases: ["Función de ventana", "función de ventana", "funciones de ventana", "window function"]
categoria: "sql"
tags: ["concepto"]
---

# Función de ventana

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Una **función de ventana** calcula un valor para cada fila usando un conjunto de filas relacionadas con ella, definido con la cláusula `OVER`. A diferencia de una función de agregación con `GROUP BY`, no reduce el número de filas: cada fila conserva su propio resultado.

## Diferencia con GROUP BY

Con `GROUP BY`, varias filas se resumen en una. Con una función de ventana, todas las filas se conservan, y cada una recibe, por ejemplo, el total de su grupo o su posición dentro de él.

## Ejemplo

```sql
SELECT cliente_id, id AS pedido, total,
       SUM(total) OVER (PARTITION BY cliente_id) AS gasto_total_cliente,
       ROW_NUMBER() OVER (PARTITION BY cliente_id ORDER BY total DESC) AS posicion
FROM pedidos;
```

`PARTITION BY` divide las filas en grupos independientes, y `ORDER BY` define el orden dentro de cada grupo.

## Funciones de ventana frecuentes

* `ROW_NUMBER()`: numera las filas dentro de cada partición, sin repetir números.
* `RANK()` y `DENSE_RANK()`: asignan posiciones; `RANK` deja huecos tras empates y `DENSE_RANK` no.
* `LAG()` y `LEAD()`: obtienen el valor de una fila anterior o posterior, útiles para comparar periodos.
* `SUM() OVER` y `AVG() OVER`: calculan totales o promedios acumulados o por grupo, sin reducir las filas.

## Ver también

* [CTE](cte.md): suelen usarse juntas para preparar los datos.
* [SQL](sql.md): el lenguaje en el que se escriben.
