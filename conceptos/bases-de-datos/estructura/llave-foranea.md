---
titulo: "Llave foránea (FK)"
aliases: ["Llave foránea (FK)", "llave foránea", "llave foranea", "clave foránea", "FK"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Llave foránea (FK)

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **llave foránea** (FK, *foreign key*) es un atributo de una tabla que referencia la llave primaria de otra tabla, o de la misma. Establece el vínculo lógico entre las filas de ambas tablas y permite que el motor rechace datos que apunten a filas que no existen.

## Integridad referencial

* El valor de la llave foránea debe existir en la tabla referenciada, o ser `NULL` si la columna lo permite.
* Al eliminar una fila referenciada, el motor puede impedirlo o aplicar una acción: `CASCADE` elimina también las filas dependientes, y `SET NULL` deja la referencia vacía.

## Ejemplo en MySQL

```sql
CREATE TABLE pedidos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

Con esta definición no es posible registrar un pedido para un cliente que no existe.

## Ver también

* [Llave primaria (PK)](llave-primaria.md): la llave a la que se hace referencia.
* [Relación entre entidades](../modelado/relacion.md): lo que la llave foránea implementa en el modelo relacional.
