---
titulo: "Cardinalidad"
aliases: ["Cardinalidad", "cardinalidad", "cardinalidades"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Cardinalidad

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

La **cardinalidad** indica cuántas ocurrencias de una entidad pueden relacionarse con cuántas ocurrencias de otra. Se expresa con mínimos y máximos, como `0..1` o `1..*`, o con los nombres uno a uno, uno a muchos y muchos a muchos.

## Tipos

* **Uno a uno (1:1):** cada cliente tiene un solo domicilio registrado, y cada domicilio pertenece a un solo cliente.
* **Uno a muchos (1:N):** un cliente puede tener muchos pedidos, pero cada pedido pertenece a un solo cliente.
* **Muchos a muchos (N:M):** un pedido puede contener muchos productos, y un producto puede aparecer en muchos pedidos.

## Implementación en el modelo relacional

Una relación 1:N se implementa con una [llave foránea](../estructura/llave-foranea.md) en la tabla del lado "muchos". Una relación N:M requiere una tabla intermedia con dos llaves foráneas.

## Ver también

* [Relación entre entidades](relacion.md): la asociación a la que se aplica la cardinalidad.
* [Modelo lógico relacional](modelo-logico-relacional.md): donde la cardinalidad se convierte en claves.
