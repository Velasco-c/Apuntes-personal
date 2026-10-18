---
titulo: "Tabla"
aliases: ["Tabla", "tabla", "tablas"]
categoria: "bases-de-datos/estructura"
tags: ["concepto"]
---

# Tabla

<!-- auto:categoria -->
Categoría: [Bases de datos › Estructura y claves](categoria.md)
<!-- /auto:categoria -->

Una **tabla** es la estructura básica de una base de datos relacional. Organiza la información en filas y columnas: cada columna define un atributo con un tipo de dato, y cada fila representa una ocurrencia de la entidad.

## Componentes

* **Nombre:** identifica la tabla dentro de la base de datos.
* **Columnas:** cada una tiene un nombre, un tipo de dato y, opcionalmente, restricciones como `NOT NULL`.
* **Filas:** los registros almacenados. En el modelo relacional se llaman [tuplas](tupla.md).
* **Llave primaria:** identifica cada fila de forma única.

## Ejemplo

```sql
CREATE TABLE productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL
);
```

## Tabla frente a vista

Una tabla almacena datos. Una [vista](vista.md) es una consulta guardada que se consulta como si fuera una tabla, pero no guarda datos propios.

## Ver también

* [Tupla](tupla.md): cada fila de la tabla.
* [Atributo](../modelado/atributo.md): de donde provienen las columnas.
