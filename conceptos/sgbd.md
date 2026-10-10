---
titulo: "Sistema Gestor de Base de Datos (SGBD)"
aliases: ["SGBD", "sistema gestor de bases de datos", "sistema de gestión de bases de datos"]
tags: ["concepto"]
---

# Sistema Gestor de Base de Datos (SGBD)
Un **SGBD** es una capa de software compleja que actúa como intermediario entre los usuarios finales y los datos almacenados físicamente. Su propósito es abstraer al usuario de la complejidad técnica del almacenamiento.

## Arquitectura y Funciones
- **[Persistencia](persistencia.md) ([ACID](transaccion.md)):** Asegura que los datos sobrevivan a fallos del sistema o reinicios, garantizando la durabilidad.
- **Independencia de datos:** Permite modificar la estructura física sin alterar las aplicaciones que consumen los datos.
- **Control Centralizado:** Gestión de acceso, seguridad, integridad y concurrencia.
- **Motor de Consultas:** Traduce lenguajes de alto nivel (como [SQL](sql.md)) a operaciones físicas optimizadas.

*Ver también: [Base de Datos](base-de-datos.md)*

<!-- auto:backlinks -->
## Dónde aparece

- [PostgreSQL](../postgresql/01-introduccion.md) · PostgreSQL · 10 menciones
- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 4 menciones
- [PostgreSQL — Configuración, administración y consultas](../postgresql/02-configuracion-administracion-y-consultas.md) · PostgreSQL · 4 menciones
- [Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual](../bases-de-datos/clase-06-fundamentos-de-diseno.md) · Bases de datos · 3 menciones
- [Persistencia de Datos en Bases de Datos Relacionales con MySQL y Node.js](../nodejs/08-persistencia-con-mysql.md) · Node.js · 3 menciones
- [Clase 02: Base de datos](../bases-de-datos/clase-02-base-de-datos.md) · Bases de datos · 2 menciones
- [MySQL — Historia, Evolución, Características y Herramientas](../mysql/01-historia-y-caracteristicas.md) · MySQL · 2 menciones
- [SQL — Fundamentos, Características, Clasificación, Tipos de Datos y Consultas](../mysql/02-fundamentos-de-sql.md) · MySQL · 2 menciones
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 1 mención

## Conceptos cercanos

[Información](informacion.md), [Tabla (Base de Datos)](tabla.md), [Base de Datos](base-de-datos.md), [Llave Primaria (PK)](llave-primaria.md), [Base de Datos Relacional](base-de-datos-relacional.md), [Índice](indice.md), [SQL](sql.md), [Atributo](atributo.md)
<!-- /auto:backlinks -->
