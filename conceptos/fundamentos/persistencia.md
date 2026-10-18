---
titulo: "Persistencia de datos"
aliases: ["Persistencia de datos", "persistencia", "persistir"]
categoria: "fundamentos"
tags: ["concepto"]
---

# Persistencia de datos

<!-- auto:categoria -->
Categoría: [Fundamentos](categoria.md)
<!-- /auto:categoria -->

**Persistencia de datos** es la capacidad de conservar información más allá de la ejecución del programa que la creó. Si los datos viven solo en memoria, se pierden cuando el proceso termina. Si se guardan en un archivo o en una base de datos, siguen disponibles en la siguiente ejecución.

## Medios de persistencia

* **Archivos** (texto, JSON, CSV): sencillos, pero difíciles de consultar y de proteger cuando varios procesos escriben a la vez.
* **Bases de datos**: permiten consultas, relaciones, transacciones y control de acceso.
* **Memoria o caché**: muy rápidas, pero temporales salvo que se configuren para conservar los datos.

## Ejemplo

Un arreglo de usuarios en un programa Node.js existe solo mientras el proceso se ejecuta. Al reiniciar el servidor, el arreglo vuelve a estar vacío. Guardar esos usuarios en una tabla de [MySQL](../motores/mysql.md) hace que sigan disponibles después del reinicio.

## Ver también

* [Base de datos](../bases-de-datos/base-de-datos.md): el medio de persistencia más usado en aplicaciones.
* [Dato](dato.md): la unidad que se persiste.
