---
titulo: "Prepared statement"
aliases: ["Prepared statement", "prepared statement", "prepared statements", "consulta preparada", "consultas preparadas", "sentencia preparada"]
categoria: "acceso-a-datos"
tags: ["concepto"]
---

# Prepared statement

<!-- auto:categoria -->
Categoría: [Acceso a datos desde una aplicación](categoria.md)
<!-- /auto:categoria -->

Una **sentencia preparada** (*prepared statement*) es una consulta SQL cuya estructura se envía al motor por separado de sus valores. Los valores se indican con marcadores de posición, como `?` en MySQL o `$1` en PostgreSQL, y el motor los trata siempre como datos, nunca como parte de la instrucción.

## Ventajas

* **Seguridad:** los valores no pueden modificar la estructura de la consulta, lo que evita la [inyección SQL](inyeccion-sql.md).
* **Rendimiento:** el motor puede analizar la consulta una vez y reutilizarla con distintos valores.

## Ejemplo con mysql2

```javascript
const [filas] = await pool.execute(
    'SELECT * FROM productos WHERE id = ?',
    [req.params.id]
);
```

## Errores comunes

Los marcadores de posición sirven para **valores**, no para nombres de tablas o de columnas. Si un nombre de columna viene del usuario, no puede pasarse como `?`. En ese caso debe validarse contra una lista permitida antes de construir la consulta. Tampoco protege una consulta que ya se construyó concatenando texto antes de llegar a `execute`.

## Ver también

* [Inyección SQL](inyeccion-sql.md): el ataque que este mecanismo evita.
* [Controlador de base de datos](controlador-de-base-de-datos.md): la biblioteca que ejecuta la sentencia preparada.
