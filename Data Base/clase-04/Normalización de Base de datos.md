## Optimización y Estructura Relacional

La normalización es un proceso sistemático de organización de datos en una base de datos relacional. Consiste en aplicar una serie de reglas, denominadas **Formas Normales (FN)**, diseñadas para estructurar las tablas de manera que se minimice la redundancia y se maximice la integridad referencial. Un diseño normalizado no solo optimiza el rendimiento y el almacenamiento, sino que también garantiza la consistencia de la información al realizar operaciones de manipulación (inserción, actualización y eliminación).

### Primera Forma Normal (1FN): Atomicidad y Estructura

Una tabla cumple con la 1FN cuando su estructura garantiza la unicidad y la indivisibilidad de sus datos.

- **Condiciones:**
    
    - **[Atomicidad](../conceptos/Atomicidad.md):** Cada celda debe contener un valor único e indivisible.
        
    - **Ausencia de repetición:** No deben existir grupos repetitivos o listas dentro de un mismo campo.
        
    - **Identificación:** Cada registro debe poseer una clave primaria (_[FK](../conceptos/Llave_Primaria.md)_) única.
        
    - **Integridad:** No se permiten filas ni columnas duplicadas.

### Segunda Forma Normal (2FN): Dependencia Total

La 2FN se enfoca en las tablas que poseen **claves primarias compuestas** (aquellas formadas por dos o más columnas).

- **Condiciones:**
    
    - Estar previamente en 1FN.
        
    - **Eliminación de dependencias parciales:** Todos los atributos que no forman parte de la clave primaria deben depender funcionalmente de la **totalidad** de la clave primaria, y no solo de una parte de ella.
        
- **Regla de oro:** "Depender de la clave, toda la clave y nada más que la clave". Si un atributo depende solo de un fragmento de la clave compuesta, debe ser segregado a una nueva [tabla](../conceptos/Tabla_(Base_de_Datos).md) donde dicho fragmento sea la clave principal.

### Tercera Forma Normal (3FN): Eliminación de Dependencias Transitivas

La 3FN asegura que los datos no sufran redundancia al depender de atributos intermedios que no son claves.

- **Condiciones:**
    
    - Estar previamente en 2FN.
        
    - **Eliminación de dependencias transitivas:** Un atributo no clave no debe depender de otro atributo no clave.
        
- **Mecanismo:** Si tenemos una relación $A \rightarrow B$ y $B \rightarrow C$, entonces $A \rightarrow C$ constituye una dependencia transitiva. Para cumplir la 3FN, el atributo $C$ debe depender directamente de la [clave primaria](../conceptos/Llave_Primaria.md) ($A$), eliminando el paso intermedio por $B$.