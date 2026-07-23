### [SGBD](../conceptos/SGBD.md)

**Descripción:** Software diseñado para administrar, consultar y persistir información de manera estructurada.
**Funciones clave:**
* **Persistencia:** Evita que los datos sean volátiles (asegura que permanezcan tras apagar el sistema).
* **Administración:** Permite el control centralizado de los datos.
* **Consulta:** Facilita la recuperación de información mediante lenguajes específicos.
* **Relacionado con:** [Base de datos](../conceptos/Base_de_Datos.md)

---

### [Base de datos](../conceptos/Base_de_Datos.md)

**Definición:** Colección de datos lógicamente coherentes, ordenados y estructurados con un significado inherente.
**Objetivo:**

* Representar elementos y usuarios del mundo real.
* Diseñarse, construirse y rellenarse con datos para un propósito específico, atendiendo a usuarios y aplicaciones determinadas.

**Conceptos base:**

* **[Entidad](../conceptos/Entidad.md):** Objeto o elemento del mundo real al cual se le pueden atribuir características o atributos.
* **[Dato](../conceptos/Dato.md):** Valor bruto representado en múltiples tipos (archivos, números, caracteres). Es aquello que puedo observar y describir.
* **[Información](../conceptos/Información.md):** Datos procesados que tienen un significado o contexto.

**Reflexión:** Una [Base de datos](../conceptos/Base_de_Datos.md) es, en esencia, un conjunto de datos organizados para generar información útil.

---

### [SGBD](../conceptos/SGBD.md)

**Definición:** Aplicación de software que actúa como intermediario entre los datos y los usuarios.
**Composición:**
* **Datos interrelacionados:** La información no está aislada.
* **Conjunto de programas:** Herramientas para acceder, gestionar y manipular la información de forma eficiente.

---

### [Tabla (Base de datos)](../conceptos/Tabla_(Base_de_Datos).md)

**Descripción:** Mecanismos para garantizar la integridad y establecer conexiones entre estructuras de datos.
* **[Llave Primaria](../conceptos/Llave_Primaria.md)(PK):** Identificador único dentro de una tabla. Garantiza que no existan duplicados (ej. un ID personal).
* **[Llave Foránea](../conceptos/Llave_Foránea.md)(FK):** Puente entre tablas. Columna en una tabla "hija" que referencia a la Llave Primaria de una tabla "padre".
* **Nota:** Es correcto darle contextos a las entidades ayuda a facilitar el consumo de la información.

---

### [Base de Datos Relacional](../conceptos/Base_de_Datos_Relacional.md)

**Definición:** Modelo de base de datos que organiza la información en [Tabla](../conceptos/Tabla_(Base_de_Datos).md) (o relaciones).
**Características:**

* **Relacionalidad:** Los registros (tuplas) se conectan mediante [llaves](../conceptos/Llaves_(Base_de_Datos).md) que coinciden en sus atributos.
* **Estructura:** Basada en filas (tuplas) y columnas (atributos).
* **Representación:** Cada tabla busca modelar una [Entidad](../conceptos/Entidad.md) de la vida real.

---

### [MER](../conceptos/MER.md)

**Definición:** Herramienta utilizada en la etapa de diseño conceptual para definir la estructura de la base de datos antes de implementarla físicamente.
**Componentes Visuales (Diagrama E-R):**

* **[Entidad](../conceptos/Entidad.md):** Objetos o conceptos de interés del mundo real. Se representan mediante rectángulos.
* **[Atributos](../conceptos/Atributo.md):** Propiedades o características que describen a la entidad. Se representan mediante óvalos.
* **[Relación](../conceptos/Relación.md):** Vínculo semántico entre entidades.
* **Nota:** Este modelo se traduce posteriormente a tablas relacionales.

---

### [Cardinalidad](../conceptos/Cardinalidad.md)

**Definición:** Define el número de elementos de una entidad que pueden asociarse con elementos de otra entidad mediante una relación.
**Tipos principales:**

* **Uno a uno (1:1):** Un registro de A se relaciona con un solo registro de B.
* **Uno a muchos (1:N):** Un registro de A se relaciona con varios de B.
* **Muchos a muchos (N:M):** Varios registros de A se relacionan con varios de B.