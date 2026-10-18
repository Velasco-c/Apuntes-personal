---
titulo: "Entidad"
aliases: ["Entidad", "entidad", "entidades"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Entidad

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

Una **entidad** es la representación de un objeto, persona, concepto o evento del mundo real que es relevante para el sistema y sobre el que se almacena información. Ejemplos: Cliente, Producto o Pedido.

## Tipo de entidad y ocurrencia

El tipo de entidad, Cliente, describe la forma general. Cada cliente concreto es una ocurrencia. En una tabla, cada ocurrencia corresponde a una fila, que se llama [tupla](../estructura/tupla.md) en el modelo relacional.

## Características

* Tiene un identificador que la distingue de las demás ocurrencias, normalmente una [llave](../estructura/llave.md).
* Tiene [atributos](atributo.md) que la describen.
* Puede participar en [relaciones](relacion.md) con otras entidades.

## Entidad débil

Una entidad débil no tiene identificador propio: depende de otra entidad para existir. Por ejemplo, una línea de pedido solo tiene sentido dentro de un pedido.

## Ver también

* [Atributo](atributo.md): las propiedades de la entidad.
* [Modelo entidad-relación (MER)](mer.md): el diagrama donde se representan las entidades.
