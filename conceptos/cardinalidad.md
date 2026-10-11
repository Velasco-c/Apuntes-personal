---
titulo: "Cardinalidad"
aliases: ["cardinalidad", "cardinalidades"]
tags: ["concepto"]
---

# Cardinalidad

Restricción que define el número de ocurrencias de una [Entidad](entidad.md) que pueden relacionarse con otra en un [MER](mer.md).

## Tipos de cardinalidad:
- **1:1 (Uno a uno):** Un registro se asocia exclusivamente a otro.
- **1:N (Uno a muchos):** Un registro padre se asocia con múltiples registros hijos.
- **M:N (Muchos a muchos):** Requiere una **[tabla](tabla.md) asociativa** (tabla intermedia) para descomponer la relación en dos de tipo 1:N.

<!-- auto:backlinks -->
## Dónde aparece

- [Modelo Entidad-Relación y consultas avanzadas en MySQL](../mysql/06-modelo-er-y-consultas-avanzadas.md) · MySQL · 10 menciones
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 4 menciones
- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 3 menciones
- [Clase 02: Base de datos](../bases-de-datos/clase-02-base-de-datos.md) · Bases de datos · 1 mención

## Conceptos cercanos

- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Entidad](entidad.md): Representación abstracta de un objeto, persona, concepto o evento del mundo real que es relevante para el sistema de información.
- [Atributo](atributo.md): Propiedad o característica que describe a una Entidad en el modelo de datos.
- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Llave Primaria (PK)](llave-primaria.md): Un Atributo o conjunto de atributos que identifica de manera única e inequívoca a cada Tupla dentro de una Tabla.
- [Llave Foránea (FK)](llave-foranea.md): Un campo en una tabla que establece un vínculo lógico con la Llave Primaria de otra tabla (o la misma).
<!-- /auto:backlinks -->
