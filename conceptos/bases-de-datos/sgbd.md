---
titulo: "Sistema gestor de bases de datos (SGBD)"
aliases: ["Sistema gestor de bases de datos (SGBD)", "SGBD", "sistema gestor de bases de datos", "DBMS"]
categoria: "bases-de-datos"
tags: ["concepto"]
---

# Sistema gestor de bases de datos (SGBD)

<!-- auto:categoria -->
Categoría: [Bases de datos](categoria.md)
<!-- /auto:categoria -->

Un **sistema gestor de bases de datos (SGBD)** es el software que crea, administra y da acceso a las bases de datos. Actúa como intermediario entre los usuarios y las aplicaciones, por un lado, y los datos almacenados físicamente, por otro.

## Funciones principales

* **Definición de datos:** crear tablas, índices y restricciones.
* **Manipulación de datos:** ejecutar consultas y cambios, normalmente con [SQL](../sql/sql.md).
* **Control de concurrencia:** permite que varios usuarios lean y escriban sin corromper los datos, apoyándose en las [transacciones](transaccion.md).
* **Seguridad:** usuarios, permisos y autenticación.
* **Recuperación:** restaurar los datos después de un fallo.

## Ejemplos

[MySQL](../motores/mysql.md) y [PostgreSQL](../motores/postgresql.md) son SGBD relacionales. El concepto es general: sirve para describir cualquier motor, no solo uno en particular.

## Ver también

* [Base de datos](base-de-datos.md): lo que administra el SGBD.
* [Transacción](transaccion.md): el mecanismo que evita datos inconsistentes cuando hay acceso simultáneo.
