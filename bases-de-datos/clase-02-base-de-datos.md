---
titulo: "Clase 02: Base de datos"
area: "bases-de-datos"
orden: 2
tags: ["bases-de-datos"]
---

# Clase 02: Base de datos

## [SGBD](../conceptos/sgbd.md)

**Descripción:** Software diseñado para administrar, consultar y [persistir](../conceptos/persistencia.md) información de manera estructurada.
**Funciones clave:**
* **Persistencia:** Evita que los datos sean volátiles (asegura que permanezcan tras apagar el sistema).
* **Administración:** Permite el control centralizado de los datos.
* **Consulta:** Facilita la recuperación de información mediante lenguajes específicos.
* **Relacionado con:** [Base de datos](../conceptos/base-de-datos.md)

---

## [Base de datos](../conceptos/base-de-datos.md)

**Definición:** Colección de datos lógicamente coherentes, ordenados y estructurados con un significado inherente.
**Objetivo:**

* Representar elementos y usuarios del mundo real.
* Diseñarse, construirse y rellenarse con datos para un propósito específico, atendiendo a usuarios y aplicaciones determinadas.

**Conceptos base:**

* **[Entidad](../conceptos/entidad.md):** Objeto o elemento del mundo real al cual se le pueden atribuir características o atributos.
* **[Dato](../conceptos/dato.md):** Valor bruto representado en múltiples tipos (archivos, números, caracteres). Es aquello que puedo observar y describir.
* **[Información](../conceptos/informacion.md):** Datos procesados que tienen un significado o contexto.

**Reflexión:** Una [Base de datos](../conceptos/base-de-datos.md) es, en esencia, un conjunto de datos organizados para generar información útil.

---

## [SGBD](../conceptos/sgbd.md)

**Definición:** Aplicación de software que actúa como intermediario entre los datos y los usuarios.
**Composición:**
* **Datos interrelacionados:** La información no está aislada.
* **Conjunto de programas:** Herramientas para acceder, gestionar y manipular la información de forma eficiente.

---

## [Tabla (Base de datos)](../conceptos/tabla.md)

**Descripción:** Mecanismos para garantizar la integridad y establecer conexiones entre estructuras de datos.
* **[Llave Primaria](../conceptos/llave-primaria.md)(PK):** Identificador único dentro de una tabla. Garantiza que no existan duplicados (ej. un ID personal).
* **[Llave Foránea](../conceptos/llave-foranea.md)(FK):** Puente entre tablas. Columna en una tabla "hija" que referencia a la Llave Primaria de una tabla "padre".
* **Nota:** Es correcto darle contextos a las entidades ayuda a facilitar el consumo de la información.

---

## [Base de Datos Relacional](../conceptos/base-de-datos-relacional.md)

**Definición:** Modelo de base de datos que organiza la información en [Tabla](../conceptos/tabla.md) (o relaciones).
**Características:**

* **Relacionalidad:** Los registros ([tuplas](../conceptos/tupla.md)) se conectan mediante [llaves](../conceptos/llaves.md) que coinciden en sus atributos.
* **Estructura:** Basada en filas (tuplas) y columnas (atributos).
* **Representación:** Cada tabla busca modelar una [Entidad](../conceptos/entidad.md) de la vida real.

---

## [MER](../conceptos/mer.md)

**Definición:** Herramienta utilizada en la etapa de diseño conceptual para definir la estructura de la base de datos antes de implementarla físicamente.
**Componentes Visuales (Diagrama E-R):**

* **[Entidad](../conceptos/entidad.md):** Objetos o conceptos de interés del mundo real. Se representan mediante rectángulos.
* **[Atributos](../conceptos/atributo.md):** Propiedades o características que describen a la entidad. Se representan mediante óvalos.
* **[Relación](../conceptos/relacion.md):** Vínculo semántico entre entidades.
* **Nota:** Este modelo se traduce posteriormente a tablas relacionales.

---

## [Cardinalidad](../conceptos/cardinalidad.md)

**Definición:** Define el número de elementos de una entidad que pueden asociarse con elementos de otra entidad mediante una relación.
**Tipos principales:**

* **Uno a uno (1:1):** Un registro de A se relaciona con un solo registro de B.
* **Uno a muchos (1:N):** Un registro de A se relaciona con varios de B.
* **Muchos a muchos (N:M):** Varios registros de A se relacionan con varios de B.

<!-- auto:pie -->
---

**Navegación:** [Índice de Bases de datos](indice.md) · [Siguiente: Clase 03: Del Diseño Conceptual al Modelo Físico →](clase-03-diseno-conceptual-a-fisico.md)

**Conceptos de esta lección:** [Información](../conceptos/informacion.md), [Entidad](../conceptos/entidad.md), [Tabla (Base de Datos)](../conceptos/tabla.md), [Base de Datos](../conceptos/base-de-datos.md), [Atributo](../conceptos/atributo.md), [Llave Primaria (PK)](../conceptos/llave-primaria.md), [Sistema Gestor de Base de Datos (SGBD)](../conceptos/sgbd.md), [Persistencia de datos](../conceptos/persistencia.md), [Llave Foránea (FK)](../conceptos/llave-foranea.md), [Tupla](../conceptos/tupla.md), [Dato](../conceptos/dato.md), [Base de Datos Relacional](../conceptos/base-de-datos-relacional.md), [Llaves (Base de Datos)](../conceptos/llaves.md), [Modelo Entidad-Relación (MER)](../conceptos/mer.md), [Cardinalidad](../conceptos/cardinalidad.md)
<!-- /auto:pie -->
