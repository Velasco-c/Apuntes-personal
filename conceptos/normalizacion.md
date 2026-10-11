---
titulo: "Normalización"
aliases: ["normalización", "normalizacion", "normalizar", "normalizado", "normalizada", "normalizaciones"]
tags: ["concepto"]
---

# Normalización

Proceso de diseño que organiza las [tablas](tabla.md) para reducir la redundancia y evitar anomalías al insertar, actualizar o borrar datos.

## Puntos clave

- 1FN: cada [atributo](atributo.md) guarda valores atómicos y no hay grupos repetidos.
- 2FN: todo atributo no clave depende de la [llave primaria](llave-primaria.md) completa.
- 3FN: ningún atributo no clave depende de otro atributo no clave.

<!-- auto:backlinks -->
## Dónde aparece

- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 4 menciones
- [Diseño de bases de datos: índices, vistas, claves y restricciones](../mysql/05-indices-vistas-y-restricciones.md) · MySQL · 4 menciones
- [Clase 04: Normalización de base de datos](../bases-de-datos/clase-04-normalizacion.md) · Bases de datos · 3 menciones
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 1 mención
- [Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual](../bases-de-datos/clase-06-fundamentos-de-diseno.md) · Bases de datos · 1 mención
- [Patrones de diseño de software](../nodejs/06-patrones-de-diseno.md) · Node.js · 1 mención

## Conceptos cercanos

- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Llave Primaria (PK)](llave-primaria.md): Un Atributo o conjunto de atributos que identifica de manera única e inequívoca a cada Tupla dentro de una Tabla.
- [Llave Foránea (FK)](llave-foranea.md): Un campo en una tabla que establece un vínculo lógico con la Llave Primaria de otra tabla (o la misma).
- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Atributo](atributo.md): Propiedad o característica que describe a una Entidad en el modelo de datos.
- [Base de Datos](base-de-datos.md): Colección estructurada de datos lógicamente coherentes que representan entidades del mundo real.
<!-- /auto:backlinks -->
