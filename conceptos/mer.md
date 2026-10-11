---
titulo: "Modelo Entidad-Relación (MER)"
aliases: ["MER", "modelo entidad-relación", "modelo entidad relación", "diagrama entidad-relación"]
tags: ["concepto"]
---

# Modelo Entidad-Relación (MER)
Técnica de **modelado conceptual** utilizada en la fase de requerimientos para representar la estructura de datos mediante diagramas E-R.

## Componentes del Diagrama E-R
- **[Entidades](entidad.md):** Representadas como rectángulos. Define el "qué" se está almacenando.
- **[Atributos](atributo.md):** Representados como óvalos. Describen las propiedades intrínsecas de las entidades.
- **Relaciones:** Representadas como rombos. Definen cómo interactúan las entidades entre sí.

## Cardinalidad
Describe la restricción de multiplicidad en una relación:
1. **1:1 (Uno a uno):** Asociación exclusiva.
2. **1:N (Uno a muchos):** Un registro padre puede tener múltiples hijos.
3. **M:N (Muchos a muchos):** Requiere una **[tabla](tabla.md) intermedia** (o tabla de unión) para ser implementada en un [modelo relacional](base-de-datos-relacional.md).

<!-- auto:backlinks -->
## Dónde aparece

- [Modelo Entidad-Relación y consultas avanzadas en MySQL](../mysql/06-modelo-er-y-consultas-avanzadas.md) · MySQL · 15 menciones
- [Clase 05: Esquemas de diseño de bases de datos relacionales](../bases-de-datos/clase-05-esquemas-de-diseno.md) · Bases de datos · 3 menciones
- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 2 menciones
- [Clase 02: Base de datos](../bases-de-datos/clase-02-base-de-datos.md) · Bases de datos · 1 mención

## Conceptos cercanos

- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
- [Entidad](entidad.md): Representación abstracta de un objeto, persona, concepto o evento del mundo real que es relevante para el sistema de información.
- [Atributo](atributo.md): Propiedad o característica que describe a una Entidad en el modelo de datos.
- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Llave Primaria (PK)](llave-primaria.md): Un Atributo o conjunto de atributos que identifica de manera única e inequívoca a cada Tupla dentro de una Tabla.
- [Llave Foránea (FK)](llave-foranea.md): Un campo en una tabla que establece un vínculo lógico con la Llave Primaria de otra tabla (o la misma).
<!-- /auto:backlinks -->
