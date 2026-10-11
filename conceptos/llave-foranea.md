---
titulo: "Llave Foránea (FK)"
aliases: ["llave foránea", "llaves foráneas", "llave foranea", "clave foránea", "claves foráneas", "FK"]
tags: ["concepto"]
---

# Llave Foránea (FK)

Un campo en una [tabla](tabla.md) que establece un vínculo lógico con la [Llave Primaria](llave-primaria.md) de otra tabla (o la misma).

## Propósito:
- **Integridad Referencial:** Garantiza que no existan relaciones "huérfanas". El valor en la FK debe existir previamente en la tabla padre referenciada.
	- **Conectividad:** Es el componente técnico que permite la navegación entre datos relacionales.

<!-- auto:backlinks -->
## Dónde aparece

- [Consultas básicas con SQL](../mysql/03-consultas-basicas.md) · MySQL · 14 menciones
- [Diseño de bases de datos: índices, vistas, claves y restricciones](../mysql/05-indices-vistas-y-restricciones.md) · MySQL · 12 menciones
- [Administración de conjuntos de datos semiestructurados y datos binarios](../postgresql/07-datos-semiestructurados-y-binarios.md) · PostgreSQL · 4 menciones
- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 4 menciones
- [SQL — Alias, funciones, JOIN, subconsultas y diseño de bases de datos](../mysql/04-alias-funciones-join-y-subconsultas.md) · MySQL · 3 menciones
- [Clase 02: Base de datos](../bases-de-datos/clase-02-base-de-datos.md) · Bases de datos · 2 menciones
- [Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual](../bases-de-datos/clase-06-fundamentos-de-diseno.md) · Bases de datos · 2 menciones
- [Persistencia de Datos en Bases de Datos Relacionales con MySQL y Node.js](../nodejs/08-persistencia-con-mysql.md) · Node.js · 2 menciones
- [Clase 04: Normalización de base de datos](../bases-de-datos/clase-04-normalizacion.md) · Bases de datos · 1 mención
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 1 mención
- [Modelo Entidad-Relación y consultas avanzadas en MySQL](../mysql/06-modelo-er-y-consultas-avanzadas.md) · MySQL · 1 mención
- [MySQL — Historia, Evolución, Características y Herramientas](../mysql/01-historia-y-caracteristicas.md) · MySQL · 1 mención

## Conceptos cercanos

- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Base de Datos](base-de-datos.md): Colección estructurada de datos lógicamente coherentes que representan entidades del mundo real.
- [Llave Primaria (PK)](llave-primaria.md): Un Atributo o conjunto de atributos que identifica de manera única e inequívoca a cada Tupla dentro de una Tabla.
- [Base de Datos Relacional](base-de-datos-relacional.md): Modelo que organiza la información en tablas interconectadas.
- [SQL](sql.md): Lenguaje estándar para definir, consultar y manipular datos en bases de datos relacionales.
<!-- /auto:backlinks -->
