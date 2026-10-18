---
titulo: "Relación entre entidades"
aliases: ["Relación entre entidades", "relación entre entidades", "relaciones entre entidades"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Relación entre entidades

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

Una **relación** es una asociación entre dos o más entidades que describe cómo se vinculan sus ocurrencias. Por ejemplo, *Cliente realiza Pedido* relaciona a un cliente con sus pedidos.

## Grado de una relación

* **Binaria:** une dos entidades. Es la más común.
* **Ternaria:** une tres entidades.
* **Recursiva:** una entidad se relaciona consigo misma, por ejemplo Empleado supervisa a Empleado.

## Representación

En el [MER](mer.md), la relación se dibuja como un rombo entre las entidades. En el modelo relacional se implementa con una [llave foránea](../estructura/llave-foranea.md) o, si es de muchos a muchos, con una tabla intermedia.

## Cómo se lee una relación

Una relación se lee como una frase en ambos sentidos. Por ejemplo, *Cliente realiza Pedido* se lee desde el cliente ("un cliente realiza uno o muchos pedidos") y desde el pedido ("un pedido es realizado por un cliente"). Leer el diagrama en las dos direcciones ayuda a verificar las cardinalidades.

## Relaciones con atributos

Una relación también puede tener atributos propios. Por ejemplo, *Estudiante se inscribe en Curso* puede tener el atributo `fecha_inscripcion`, que no pertenece ni al estudiante ni al curso, sino a la inscripción.

## Ver también

* [Cardinalidad](cardinalidad.md): cuántas ocurrencias participan en cada lado.
* [Entidad](entidad.md): los elementos que une la relación.
