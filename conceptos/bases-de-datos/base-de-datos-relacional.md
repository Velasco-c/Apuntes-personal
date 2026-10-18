---
titulo: "Base de datos relacional"
aliases: ["Base de datos relacional", "base de datos relacional", "bases de datos relacionales"]
categoria: "bases-de-datos"
tags: ["concepto"]
---

# Base de datos relacional

<!-- auto:categoria -->
Categoría: [Bases de datos](categoria.md)
<!-- /auto:categoria -->

Una **base de datos relacional** organiza la información en [tablas](estructura/tabla.md) relacionadas entre sí mediante claves. Cada tabla representa un tipo de entidad, cada fila representa una ocurrencia y cada columna representa un atributo.

## Principios

* Los datos se agrupan en tablas con columnas de tipo definido.
* Cada fila se identifica con una [llave primaria](estructura/llave-primaria.md).
* Una [llave foránea](estructura/llave-foranea.md) apunta a la fila de otra tabla, y así se expresan las relaciones.
* Las consultas se escriben en [SQL](../sql/sql.md) y pueden combinar tablas con [JOIN](../sql/join.md).
* Las restricciones (tipos, valores obligatorios, claves) protegen la integridad de los datos.

## Ejemplo

```text
clientes(id, nombre)
pedidos(id, cliente_id, total)
```

En este esquema, `pedidos.cliente_id` es una llave foránea que referencia a `clientes.id`. Cada pedido pertenece a un único cliente, y un cliente puede tener varios pedidos.

## Ver también

* [Modelo lógico relacional](modelado/modelo-logico-relacional.md): cómo se traduce un diseño de entidades a tablas.
* [MySQL](../motores/mysql.md) y [PostgreSQL](../motores/postgresql.md): motores que implementan el modelo relacional.
