---
titulo: "Llave Primaria (PK)"
aliases: ["llave primaria", "llaves primarias", "clave primaria", "claves primarias", "PK"]
tags: ["concepto"]
---

# Llave Primaria (PK)

Un [Atributo](atributo.md) o conjunto de [atributos](atributo.md) que identifica de manera única e inequívoca a cada [Tupla](tupla.md) dentro de una [Tabla](tabla.md).

## Requisitos de integridad:
1. **Unicidad:** No puede haber dos [tuplas](tupla.md) con el mismo valor en la PK.
2. **No Nulidad (Entity Integrity):** No puede ser un valor nulo (null), ya que el identificador es obligatorio.
3. **Minimalidad:** Debe ser el conjunto más pequeño posible de atributos que garantice la unicidad.

<!-- auto:backlinks -->
## Dónde aparece

- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 6 menciones
- [Diseño de bases de datos: índices, vistas, claves y restricciones](../mysql/05-indices-vistas-y-restricciones.md) · MySQL · 6 menciones
- [PostgreSQL — Configuración, administración y consultas](../postgresql/02-configuracion-administracion-y-consultas.md) · PostgreSQL · 6 menciones
- [Clase 04: Normalización de base de datos](../bases-de-datos/clase-04-normalizacion.md) · Bases de datos · 5 menciones
- [Administración de conjuntos de datos semiestructurados y datos binarios](../postgresql/07-datos-semiestructurados-y-binarios.md) · PostgreSQL · 4 menciones
- [Clase 02: Base de datos](../bases-de-datos/clase-02-base-de-datos.md) · Bases de datos · 3 menciones
- [Persistencia de Datos en Bases de Datos Relacionales con MySQL y Node.js](../nodejs/08-persistencia-con-mysql.md) · Node.js · 3 menciones
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 2 menciones
- [Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual](../bases-de-datos/clase-06-fundamentos-de-diseno.md) · Bases de datos · 2 menciones
- [SQL — Alias, funciones, JOIN, subconsultas y diseño de bases de datos](../mysql/04-alias-funciones-join-y-subconsultas.md) · MySQL · 2 menciones
- [SQL — Fundamentos, Características, Clasificación, Tipos de Datos y Consultas](../mysql/02-fundamentos-de-sql.md) · MySQL · 2 menciones
- [Consultas básicas con SQL](../mysql/03-consultas-basicas.md) · MySQL · 1 mención
- [Modelo Entidad-Relación y consultas avanzadas en MySQL](../mysql/06-modelo-er-y-consultas-avanzadas.md) · MySQL · 1 mención
- [PostgreSQL](../postgresql/01-introduccion.md) · PostgreSQL · 1 mención

## Conceptos cercanos

- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Base de Datos](base-de-datos.md): Colección estructurada de datos lógicamente coherentes que representan entidades del mundo real.
- [Llave Foránea (FK)](llave-foranea.md): Un campo en una tabla que establece un vínculo lógico con la Llave Primaria de otra tabla (o la misma).
- [Base de Datos Relacional](base-de-datos-relacional.md): Modelo que organiza la información en tablas interconectadas.
- [SQL](sql.md): Lenguaje estándar para definir, consultar y manipular datos en bases de datos relacionales.
<!-- /auto:backlinks -->
