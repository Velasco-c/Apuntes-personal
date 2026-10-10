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

[Entidad](entidad.md), [Atributo](atributo.md), [Tabla (Base de Datos)](tabla.md), [Llave Primaria (PK)](llave-primaria.md), [Llave Foránea (FK)](llave-foranea.md), [Información](informacion.md), [Modelo Entidad-Relación (MER)](mer.md), [Cardinalidad](cardinalidad.md)
<!-- /auto:backlinks -->
