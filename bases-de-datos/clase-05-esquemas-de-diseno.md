---
titulo: "Clase 05: Esquemas de diseño de bases de datos relacionales"
area: "bases-de-datos"
orden: 5
tags: ["bases-de-datos"]
---

# Clase 05: Esquemas de diseño de bases de datos relacionales

## Fundamentos del Diseño de Bases de Datos: Modelado y Representación Visual

El diseño de una [base de datos](../conceptos/bases-de-datos/base-de-datos.md) es un proceso crítico que precede a la implementación física del sistema. Para garantizar que los datos estén bien estructurados, los profesionales utilizan esquemas y diagramas que actúan como el plano arquitectónico del sistema de [información](../conceptos/fundamentos/dato.md).

### Diagramas de Bases de Datos: La Herramienta Visual

Un diagrama de base de datos es una **representación gráfica** de la estructura lógica de los datos. Esta herramienta permite visualizar tanto la totalidad de un sistema complejo como segmentos específicos del mismo, facilitando la comunicación entre desarrolladores, analistas y partes interesadas.

- **Propósito:** Actuar como un mapa que define las [tablas](../conceptos/bases-de-datos/estructura/tabla.md), los campos, las relaciones ([claves primarias](../conceptos/bases-de-datos/estructura/llave-primaria.md) y foráneas) y las restricciones de integridad antes de escribir una sola línea de código [SQL](../conceptos/sql/sql.md).
    
- **Utilidad:** Es fundamental para organizar, [normalizar](../conceptos/bases-de-datos/modelado/normalizacion.md) y validar el diseño de la base de datos, asegurando que los requerimientos del negocio se traduzcan correctamente en una estructura de almacenamiento eficiente.
    

### Diferenciación: Modelo Entidad-Relación (E-R) vs. Modelo Relacional

Aunque ambos conceptos están intrínsecamente ligados, sirven a etapas distintas del proceso de diseño:

|**Característica**|**[Modelo Entidad-Relación](../conceptos/bases-de-datos/modelado/mer.md) (E-R)**|**[Modelo Relacional](../conceptos/bases-de-datos/base-de-datos-relacional.md)**|
|---|---|---|
|**Enfoque**|Conceptual y abstracto.|Lógico y técnico.|
|**Nivel de detalle**|Define conceptos, [entidades](../conceptos/bases-de-datos/modelado/entidad.md), [atributos](../conceptos/bases-de-datos/modelado/atributo.md) y relaciones.|Define tablas, columnas, tipos de datos y claves (PK/[FK](../conceptos/bases-de-datos/estructura/llave-foranea.md)).|
|**Objetivo**|Entender el problema y los requerimientos del negocio.|Preparar la estructura para su implementación en un [SGBD](../conceptos/bases-de-datos/sgbd.md).|

- **Modelo E-R:** Se centra en "qué" información existe y cómo interactúan los conceptos del mundo real. Es independiente de cualquier tecnología de base de datos específica.
    
- **Modelo Relacional:** Es la implementación formal donde las entidades se convierten en tablas, los atributos en columnas y las relaciones en restricciones de integridad referencial.

### Ejemplo diagrama entidad-relación

_Versión en Mermaid del esquema original. Las multiplicidades se transcribieron de la imagen: `1..*` → `}|`, `0..*` → `}o`, `1..1` → `||`, `0..1` → `|o`. La línea punteada (clase de asociación) no tiene equivalente directo en Mermaid. Los tipos de [dato](../conceptos/fundamentos/dato.md) son orientativos._

```mermaid
erDiagram
    PROVEEDOR {
        string IDDeEntrega
        date FechaDeEntrega
        string IDDeProveedor
    }
    PEDIDO {
        string IDDePedido
        date FechaDelPedido
        string IDDeSedeCentral
    }
    DETALLESDELPEDIDO {
        string IDDeDetallesDelPedido
        string ID_del_producto
        string IDDePedido
        int CantidadDeProducto
    }
    PRODUCTO {
        string IDDeProveedor
        string ID_del_producto
    }
    ENTREGADEDETALLESDELPEDIDO {
        string IDDeEntrega
        string IDDePedido
        string IDDeDetallesDelPedido
    }
    SEDECENTRAL {
        string IDDeSedeCentral
        string IDDeRama
    }
    RAMA {
        string IDDeRama
    }
    ENTREGA {
        string IDDeEntrega
        date FechaDeEntrega
        string IDDeProveedor
    }
    PROVEEDOR }|--o{ PRODUCTO : relación
    PEDIDO ||--o| DETALLESDELPEDIDO : relación
    PEDIDO }o--|| SEDECENTRAL : relación
    PRODUCTO }o--|{ DETALLESDELPEDIDO : relación
    DETALLESDELPEDIDO }|--|{ ENTREGA : relación
    SEDECENTRAL ||--o{ RAMA : relación
```

### Modelado mediante Lenguaje Unificado de Modelado (UML)

El **UML (Unified Modeling Language)** es el estándar de la industria para visualizar sistemas de software. Cuando se utiliza UML para representar diagramas E-R, se aporta un nivel de estandarización que facilita la interpretación técnica.

#### La Cardinalidad en el Modelado

La [cardinalidad](../conceptos/bases-de-datos/modelado/cardinalidad.md) define la restricción numérica que rige la [relación entre entidades](../conceptos/bases-de-datos/modelado/relacion.md) (por ejemplo: uno a uno, uno a muchos, o muchos a muchos). En los esquemas UML, esta se expresa de dos formas principales:

1. **Representación Numérica:** Utiliza notación directa, como `1..1` (uno a uno), `1..*` (uno a muchos) o `0..*` (cero a muchos), para indicar claramente los límites mínimo y máximo de la relación.
    
2. **Representación Simbólica:** Emplea notaciones gráficas estandarizadas (como la notación de "pata de gallo") para indicar visualmente el tipo de relación de un vistazo.
    
## simbología

Mermaid expresa la cardinalidad con estos símbolos, que equivalen a los de la leyenda original:

- `|o` cero o uno
- `||` uno y solo uno (Mermaid no distingue entre «uno» y «uno y solo uno»)
- `}o` cero o muchos
- `}|` uno o muchos

```mermaid
erDiagram
    A |o--|| B : "cero o uno"
    C }o--|| D : "cero o muchos"
    E }|--|| F : "uno o muchos"
    G ||--|| H : "uno"
```

> **Nota técnica:** Mientras que el modelo E-R original utiliza símbolos específicos para la cardinalidad (como diamantes y líneas con etiquetas), el enfoque UML integra estas relaciones dentro de los diagramas de clases, permitiendo una transición más fluida hacia el diseño orientado a objetos y la implementación en bases de datos relacionales.

<!-- auto:pie -->
---

**Navegación:** [← Anterior: Clase 04: Normalización de base de datos](clase-04-normalizacion.md) · [Índice de Bases de datos](indice.md) · [Siguiente: Clase 06: Fundamentos del diseño de bases de datos, modelado y representación visual →](clase-06-fundamentos-de-diseno.md)
<!-- /auto:pie -->
