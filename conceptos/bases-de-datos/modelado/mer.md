---
titulo: "Modelo entidad-relación (MER)"
aliases: ["Modelo entidad-relación (MER)", "MER", "modelo entidad-relación", "modelo E-R"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Modelo entidad-relación (MER)

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

El **modelo entidad-relación (MER)** es una técnica de modelado conceptual que describe los datos de un sistema mediante entidades, atributos y relaciones, representados en un diagrama. Se usa en la fase de análisis, antes de decidir qué tablas se crearán.

## Elementos del diagrama

* **Entidad:** rectángulo. Representa un objeto o concepto, por ejemplo Cliente.
* **Atributo:** óvalo conectado a su entidad, por ejemplo nombre o correo.
* **Relación:** rombo que une dos o más entidades, por ejemplo *Cliente realiza Pedido*.
* **Cardinalidad:** indica cuántas ocurrencias participan en cada lado de la relación.

## Flujo de diseño

El MER se transforma en el [modelo lógico relacional](modelo-logico-relacional.md), que define tablas, columnas y claves. Después, ese modelo se implementa en un [SGBD](../sgbd.md) concreto.

## Ver también

* [Entidad](entidad.md): el elemento central del diagrama.
* [Relación entre entidades](relacion.md): cómo se representan las asociaciones.
