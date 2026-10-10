---
titulo: "Clase 05: Esquemas de diseño de bases de datos relacionales"
area: "bases-de-datos"
orden: 5
tags: ["bases-de-datos"]
---

# Clase 05: Esquemas de diseño de bases de datos relacionales

## Fundamentos del Diseño de Bases de Datos: Modelado y Representación Visual

El diseño de una [base de datos](../conceptos/base-de-datos.md) es un proceso crítico que precede a la implementación física del sistema. Para garantizar que los datos estén bien estructurados, los profesionales utilizan esquemas y diagramas que actúan como el plano arquitectónico del sistema de [información](../conceptos/informacion.md).

### Diagramas de Bases de Datos: La Herramienta Visual

Un diagrama de base de datos es una **representación gráfica** de la estructura lógica de los datos. Esta herramienta permite visualizar tanto la totalidad de un sistema complejo como segmentos específicos del mismo, facilitando la comunicación entre desarrolladores, analistas y partes interesadas.

- **Propósito:** Actuar como un mapa que define las [tablas](../conceptos/tabla.md), los campos, las relaciones ([claves primarias](../conceptos/llave-primaria.md) y foráneas) y las restricciones de integridad antes de escribir una sola línea de código [SQL](../conceptos/sql.md).
    
- **Utilidad:** Es fundamental para organizar, [normalizar](../conceptos/normalizacion.md) y validar el diseño de la base de datos, asegurando que los requerimientos del negocio se traduzcan correctamente en una estructura de almacenamiento eficiente.
    

### Diferenciación: Modelo Entidad-Relación (E-R) vs. Modelo Relacional

Aunque ambos conceptos están intrínsecamente ligados, sirven a etapas distintas del proceso de diseño:

|**Característica**|**[Modelo Entidad-Relación](../conceptos/mer.md) (E-R)**|**[Modelo Relacional](../conceptos/base-de-datos-relacional.md)**|
|---|---|---|
|**Enfoque**|Conceptual y abstracto.|Lógico y técnico.|
|**Nivel de detalle**|Define conceptos, [entidades](../conceptos/entidad.md), [atributos](../conceptos/atributo.md) y relaciones.|Define tablas, columnas, tipos de datos y claves (PK/[FK](../conceptos/llave-foranea.md)).|
|**Objetivo**|Entender el problema y los requerimientos del negocio.|Preparar la estructura para su implementación en un [SGBD](../conceptos/sgbd.md).|

- **Modelo E-R:** Se centra en "qué" información existe y cómo interactúan los conceptos del mundo real. Es independiente de cualquier tecnología de base de datos específica.
    
- **Modelo Relacional:** Es la implementación formal donde las entidades se convierten en tablas, los atributos en columnas y las relaciones en restricciones de integridad referencial.

### Ejemplo diagrama entidad-relación

![Esquema.png](imagenes/esquema.png)

### Modelado mediante Lenguaje Unificado de Modelado (UML)

El **UML (Unified Modeling Language)** es el estándar de la industria para visualizar sistemas de software. Cuando se utiliza UML para representar diagramas E-R, se aporta un nivel de estandarización que facilita la interpretación técnica.

#### La Cardinalidad en el Modelado

La [cardinalidad](../conceptos/cardinalidad.md) define la restricción numérica que rige la [relación entre entidades](../conceptos/relacion.md) (por ejemplo: uno a uno, uno a muchos, o muchos a muchos). En los esquemas UML, esta se expresa de dos formas principales:

1. **Representación Numérica:** Utiliza notación directa, como `1..1` (uno a uno), `1..*` (uno a muchos) o `0..*` (cero a muchos), para indicar claramente los límites mínimo y máximo de la relación.
    
2. **Representación Simbólica:** Emplea notaciones gráficas estandarizadas (como la notación de "pata de gallo") para indicar visualmente el tipo de relación de un vistazo.
    
## simbología

![Cardanalidad](imagenes/cardinalidad.png)

> **Nota técnica:** Mientras que el modelo E-R original utiliza símbolos específicos para la cardinalidad (como diamantes y líneas con etiquetas), el enfoque UML integra estas relaciones dentro de los diagramas de clases, permitiendo una transición más fluida hacia el diseño orientado a objetos y la implementación en bases de datos relacionales.

<!-- auto:pie -->
---

**Navegación:** [← Anterior: Clase 04: Normalización de base de datos](clase-04-normalizacion.md) · [Índice de Bases de datos](indice.md) · [Siguiente: Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual →](clase-06-fundamentos-de-diseno.md)

**Conceptos de esta lección:** [Base de Datos](../conceptos/base-de-datos.md), [Base de Datos Relacional](../conceptos/base-de-datos-relacional.md), [Tabla (Base de Datos)](../conceptos/tabla.md), [Modelo Entidad-Relación (MER)](../conceptos/mer.md), [Cardinalidad](../conceptos/cardinalidad.md), [Información](../conceptos/informacion.md), [Llave Primaria (PK)](../conceptos/llave-primaria.md), [Entidad](../conceptos/entidad.md), [Atributo](../conceptos/atributo.md), [SQL](../conceptos/sql.md), [Normalización](../conceptos/normalizacion.md), [Llave Foránea (FK)](../conceptos/llave-foranea.md), [Sistema Gestor de Base de Datos (SGBD)](../conceptos/sgbd.md), [Relación entre entidades](../conceptos/relacion.md)
<!-- /auto:pie -->
