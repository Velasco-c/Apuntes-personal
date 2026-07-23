# Llave Primaria (PK)

Un [Atributo](../conceptos/Atributo.md) o conjunto de atributos que identifica de manera única e inequívoca a cada [Tupla](../conceptos/Tupla.md) dentro de una [Tabla](../conceptos/Tabla_(Base_de_Datos).md).

## Requisitos de integridad:
1. **Unicidad:** No puede haber dos tuplas con el mismo valor en la PK.
2. **No Nulidad (Entity Integrity):** No puede ser un valor nulo (null), ya que el identificador es obligatorio.
3. **Minimalidad:** Debe ser el conjunto más pequeño posible de atributos que garantice la unicidad.