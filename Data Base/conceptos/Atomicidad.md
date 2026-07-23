# Atomicidad

Principio fundamental del [Modelo Relacional](../conceptos/Modelo_Relacional.md) que establece que el valor de cada [Atributo](../conceptos/Atributo.md) debe ser indivisible.

## Criterios de cumplimiento:
- **No listas:** Una celda no debe contener conjuntos, arrays o elementos separados por comas.
- **Indivisibilidad:** El valor no puede descomponerse en partes más pequeñas que tengan significado propio dentro de la aplicación.
- **Beneficio:** Facilita la consulta (SQL), la indexación y evita la redundancia de datos.

*Relacionado con: [Atributo Compuesto](../conceptos/Atributo_Compuesto), [Atributo_Multivaluado](../conceptos/Atributo_Multivaluado)*