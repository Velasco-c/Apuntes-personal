# Cardinalidad

Restricción que define el número de ocurrencias de una [Entidad](../conceptos/Entidad.md) que pueden relacionarse con otra en un [MER](../conceptos/MER.md).

## Tipos de cardinalidad:
- **1:1 (Uno a uno):** Un registro se asocia exclusivamente a otro.
- **1:N (Uno a muchos):** Un registro padre se asocia con múltiples registros hijos.
- **M:N (Muchos a muchos):** Requiere una **tabla asociativa** (tabla intermedia) para descomponer la relación en dos de tipo 1:N.