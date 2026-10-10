---
titulo: "Atomicidad"
aliases: ["atomicidad"]
tags: ["concepto"]
---

# Atomicidad

Principio fundamental del [Modelo Relacional](modelo-logico-relacional.md) que establece que el valor de cada [Atributo](atributo.md) debe ser indivisible.

## Criterios de cumplimiento:
- **No listas:** Una celda no debe contener conjuntos, arrays o elementos separados por comas.
- **Indivisibilidad:** El valor no puede descomponerse en partes más pequeñas que tengan significado propio dentro de la aplicación.
- **Beneficio:** Facilita la consulta ([SQL](sql.md)), la indexación y evita la redundancia de datos.

*Relacionado con: [Atributo Compuesto](atributo-compuesto.md), [Atributo_Multivaluado](atributo-multivaluado.md)*

<!-- auto:backlinks -->
## Dónde aparece

- [Clase 04: Normalización de base de datos](../bases-de-datos/clase-04-normalizacion.md) · Bases de datos · 2 menciones
- [MySQL — Historia, Evolución, Características y Herramientas](../mysql/01-historia-y-caracteristicas.md) · MySQL · 2 menciones
- [Optimización de Consultas, Transacciones, Particionamiento y Seguridad en MySQL](../mysql/09-optimizacion-transacciones-y-particionamiento.md) · MySQL · 2 menciones
- [PostgreSQL](../postgresql/01-introduccion.md) · PostgreSQL · 2 menciones
- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 1 mención

## Conceptos cercanos

[Tabla (Base de Datos)](tabla.md), [Información](informacion.md), [Índice](indice.md), [Base de Datos](base-de-datos.md), [Atributo](atributo.md), [Sistema Gestor de Base de Datos (SGBD)](sgbd.md), [Llave Primaria (PK)](llave-primaria.md), [Llave Foránea (FK)](llave-foranea.md)
<!-- /auto:backlinks -->
