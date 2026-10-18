---
titulo: "Índice de base de datos"
aliases: ["Índice de base de datos", "índice de base de datos", "índice", "índices", "indice", "indices"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Índice de base de datos

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Un **índice** de base de datos es una estructura auxiliar que permite localizar filas por el valor de una o más columnas sin recorrer toda la tabla. Acelera las búsquedas y los filtros, a costa de ocupar espacio y de hacer un poco más lentas las escrituras, porque el índice también debe actualizarse.

## Cómo funciona

Sin índice, el motor revisa fila por fila hasta encontrar las coincidencias. Con un índice, consulta primero una estructura ordenada, normalmente un árbol B o B+, y va directamente a las filas buscadas.

## Tipos comunes

* **Índice simple:** sobre una sola columna.
* **Índice compuesto:** sobre varias columnas, útil cuando las consultas filtran por todas ellas.
* **Índice único:** además de acelerar la búsqueda, impide valores repetidos.

Las llaves primarias y las restricciones de unicidad suelen crear un índice automáticamente.

## Ejemplo

```sql
CREATE INDEX idx_clientes_correo ON clientes (correo);
```

## Ver también

* [Tabla](tabla.md): la estructura que se indexa.
* [MySQL](../../motores/mysql.md): motor donde los índices se almacenan con InnoDB.
