---
titulo: "Principios SOLID"
aliases: ["Principios SOLID", "principios SOLID", "SOLID"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Principios SOLID

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

**SOLID** es un conjunto de cinco principios de diseño orientado a objetos que buscan código fácil de mantener, extender y probar. Cada letra corresponde a un principio.

## Los cinco principios

* **S, responsabilidad única:** una clase debe tener una sola razón para cambiar.
* **O, abierto/cerrado:** el código debe poder extenderse sin modificar lo que ya funciona.
* **L, sustitución de Liskov:** un objeto de una subclase debe poder usarse donde se espera la clase padre, sin que el programa falle.
* **I, segregación de interfaces:** conviene tener interfaces pequeñas y específicas, en lugar de una grande que obligue a implementar métodos innecesarios.
* **D, inversión de dependencias:** los módulos de alto nivel dependen de abstracciones, no de implementaciones concretas.

## Ejemplo: responsabilidad única

Un servicio que valida datos, guarda un registro en la base de datos y envía un correo incumple el primer principio. Separar esas tres tareas en componentes distintos hace que cada uno cambie por una sola razón.

## Ver también

* [Patrón de diseño](patron-de-diseno.md): soluciones que suelen aplicar estos principios.
* [Programación orientada a objetos](../programacion/poo.md): el paradigma para el que se formularon.
