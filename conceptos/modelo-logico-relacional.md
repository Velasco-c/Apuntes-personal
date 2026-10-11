---
titulo: "Modelo Lógico Relacional"
aliases: ["modelo lógico relacional", "modelo lógico", "modelo logico relacional"]
tags: ["concepto"]
---

# Modelo Lógico Relacional

Etapa de diseño donde el [MER](mer.md) se transforma en una estructura de [tablas](tabla.md) lista para ser implementada en un [SGBD](sgbd.md).

## Componentes de Diseño
1. **Definición de Campos:**
   - Nombre, descripción y validaciones (**NOT NULL** , longitud, tipo de [dato](dato.md)).
1. **Definición de Claves:**
   - [PK](llave-primaria.md): Identificador único.
   - **Claves Alternativas:** Candidatos a [PK](llave-primaria.md) no seleccionados.
   - [FK](llave-foranea.md): Vínculo referencial entre tablas.
3. **Reglas de Comportamiento:**
   - **Integridad Referencial:** Definición de acciones ante cambios (ej. `ON DELETE CASCADE`, `ON UPDATE SET NULL`).

```sql
-- Ejemplo de integridad referencial
CREATE TABLE Usuario (
    id_usuario INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255),
    rol VARCHAR(255)
);

CREATE TABLE TABLA_productos (
    id_producto INT NOT NULL PRIMARY KEY,
    nombre VARCHAR(255),
    precio DECIMAL(10,2) -- Ajustado de 255 a una escala decimal real
);
```

<!-- auto:backlinks -->
## Dónde aparece

- [Clase 03: Del Diseño Conceptual al Modelo Físico](../bases-de-datos/clase-03-diseno-conceptual-a-fisico.md) · Bases de datos · 3 menciones
- [Administración de conjuntos de datos semiestructurados y datos binarios](../postgresql/07-datos-semiestructurados-y-binarios.md) · PostgreSQL · 1 mención
- [Modelo Entidad-Relación y consultas avanzadas en MySQL](../mysql/06-modelo-er-y-consultas-avanzadas.md) · MySQL · 1 mención

## Conceptos cercanos

- [Entidad](entidad.md): Representación abstracta de un objeto, persona, concepto o evento del mundo real que es relevante para el sistema de información.
- [Atributo](atributo.md): Propiedad o característica que describe a una Entidad en el modelo de datos.
- [Tabla (Base de Datos)](tabla.md): Estructura fundamental para organizar información en filas y columnas.
- [Llave Primaria (PK)](llave-primaria.md): Un Atributo o conjunto de atributos que identifica de manera única e inequívoca a cada Tupla dentro de una Tabla.
- [Llave Foránea (FK)](llave-foranea.md): Un campo en una tabla que establece un vínculo lógico con la Llave Primaria de otra tabla (o la misma).
- [Información](informacion.md): Conjunto organizado de datos procesados que poseen un significado, contexto y propósito dentro de un sistema.
<!-- /auto:backlinks -->
