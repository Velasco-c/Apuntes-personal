# Modelo Entidad-Relación (MER)
Técnica de **modelado conceptual** utilizada en la fase de requerimientos para representar la estructura de datos mediante diagramas E-R.

## Componentes del Diagrama E-R
- **Entidades:** Representadas como rectángulos. Define el "qué" se está almacenando.
- **Atributos:** Representados como óvalos. Describen las propiedades intrínsecas de las entidades.
- **Relaciones:** Representadas como rombos. Definen cómo interactúan las entidades entre sí.

## Cardinalidad
Describe la restricción de multiplicidad en una relación:
1. **1:1 (Uno a uno):** Asociación exclusiva.
2. **1:N (Uno a muchos):** Un registro padre puede tener múltiples hijos.
3. **M:N (Muchos a muchos):** Requiere una **tabla intermedia** (o tabla de unión) para ser implementada en un modelo relacional.