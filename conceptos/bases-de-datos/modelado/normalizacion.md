---
titulo: "Normalización"
aliases: ["Normalización", "normalización", "normalizacion", "formas normales"]
categoria: "bases-de-datos/modelado"
tags: ["concepto"]
---

# Normalización

<!-- auto:categoria -->
Categoría: [Bases de datos › Modelado de datos](categoria.md)
<!-- /auto:categoria -->

La **normalización** es un proceso de diseño que organiza las tablas para reducir la redundancia y evitar anomalías al insertar, actualizar o eliminar datos. Se aplica sobre el [modelo lógico relacional](modelo-logico-relacional.md), paso a paso, mediante formas normales.

## Formas normales básicas

* **Primera forma normal (1FN):** cada columna contiene valores atómicos. No hay listas ni grupos repetidos dentro de una misma celda.
* **Segunda forma normal (2FN):** cumple la 1FN y todo atributo que no es clave depende de la clave completa, no de solo una parte de ella.
* **Tercera forma normal (3FN):** cumple la 2FN y ningún atributo que no es clave depende de otro atributo que tampoco es clave.

## Anomalías que evita

Si un mismo dato se repite en varias filas, cambiarlo en una y no en las demás deja la base de datos inconsistente. Normalizar separa esos datos en una tabla propia, a la que las demás filas hacen referencia con una [llave foránea](../estructura/llave-foranea.md).

## Ejemplo

Una tabla de pedidos que repite el nombre y el correo del cliente en cada pedido se separa en dos tablas: `clientes` y `pedidos`. El correo se modifica en un solo lugar.

## Ver también

* [Atributo](atributo.md): la atomicidad que exige la primera forma normal.
* [Modelo lógico relacional](modelo-logico-relacional.md): el modelo que se normaliza.
