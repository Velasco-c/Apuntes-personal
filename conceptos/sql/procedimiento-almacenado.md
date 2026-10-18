---
titulo: "Procedimiento almacenado"
aliases: ["Procedimiento almacenado", "procedimiento almacenado", "procedimientos almacenados", "stored procedure"]
categoria: "sql"
tags: ["concepto"]
---

# Procedimiento almacenado

<!-- auto:categoria -->
Categoría: [SQL](categoria.md)
<!-- /auto:categoria -->

Un **procedimiento almacenado** es un bloque de sentencias SQL guardado en el servidor de base de datos, que se invoca por su nombre y puede recibir parámetros. Permite encapsular lógica que se ejecuta junto a los datos.

## Ventajas y riesgos

* Reduce el tráfico entre la aplicación y la base de datos, porque la lógica se ejecuta en el servidor.
* Centraliza reglas que deben aplicarse siempre, sin importar qué aplicación consulte.
* Traslada lógica de negocio a la base de datos, lo que puede dificultar las pruebas y el mantenimiento.

## Ejemplo en MySQL

```sql
DELIMITER //
CREATE PROCEDURE obtener_productos_caros(IN minimo DECIMAL(10,2))
BEGIN
    SELECT nombre, precio FROM productos WHERE precio >= minimo;
END //
DELIMITER ;

CALL obtener_productos_caros(300);
```

## Cuándo conviene y cuándo no

Un procedimiento almacenado conviene cuando una operación compleja se repite en varias aplicaciones, o cuando se quiere limitar el acceso: se puede dar permiso de `EXECUTE` sobre el procedimiento sin dar acceso directo a las tablas. No conviene cuando la lógica cambia con frecuencia o cuando el equipo no puede mantener código en la base de datos, porque es más difícil de versionar y probar.

## Ver también

* [Trigger](trigger.md): código que se ejecuta de forma automática, no por una llamada explícita.
* [MySQL](../motores/mysql.md) y [PostgreSQL](../motores/postgresql.md): ambos los soportan con sintaxis propia.
