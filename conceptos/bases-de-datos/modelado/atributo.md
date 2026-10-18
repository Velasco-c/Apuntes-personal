---
titulo: "Atributo"
aliases: ["Atributo", "atributo", "atributos", "atributo compuesto", "atributo multivaluado"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Atributo

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

Un **atributo** es una propiedad que describe a una entidad. En una tabla, cada atributo corresponde a una columna: `nombre`, `correo` o `precio`.

## Tipos de atributo

* **Simple:** no se divide en partes. Por ejemplo, `codigo`.
* **Compuesto:** se subdivide en partes con significado propio. Por ejemplo, `direccion` puede descomponerse en calle, ciudad y código postal. En el modelo relacional se suele crear una columna por cada parte.
* **Multivaluado:** puede tomar varios valores para una misma entidad, como los teléfonos de un cliente. No debe guardarse en una sola columna; se resuelve con una tabla aparte.
* **Derivado:** se calcula a partir de otros datos, por ejemplo la edad a partir de la fecha de nacimiento. Normalmente no se almacena.

## Atributo atómico

Un atributo es atómico cuando no puede dividirse en partes que sean útiles para el sistema. Es la condición que exige la primera forma normal, explicada en [normalización](normalizacion.md).

## Ver también

* [Normalización](normalizacion.md): cómo se aplican los atributos atómicos en las tablas.
* [Entidad](entidad.md): el elemento al que pertenecen los atributos.
