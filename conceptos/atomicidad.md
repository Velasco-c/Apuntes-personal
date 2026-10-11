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

- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Índice](indice.md): Estructura auxiliar que permite localizar filas por el valor de una o más columnas sin recorrer toda la tabla.
- [Base de Datos](base-de-datos.md): Colección estructurada de datos lógicamente coherentes que representan entidades del mundo real.
- [Atributo](atributo.md): Propiedad o característica que describe a una Entidad en el modelo de datos.
- [Sistema Gestor de Base de Datos (SGBD)](sgbd.md): Un SGBD es una capa de software compleja que actúa como intermediario entre los usuarios finales y los datos almacenados físicamente.
<!-- /auto:backlinks -->
