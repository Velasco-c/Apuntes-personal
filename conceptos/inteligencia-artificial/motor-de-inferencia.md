---
titulo: "Motor de inferencia"
aliases: ["Motor de inferencia", "motor de inferencia", "motores de inferencia"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Motor de inferencia

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

Un **motor de inferencia** es el componente de un [sistema experto](sistema-experto.md) que aplica las reglas de la [base de conocimiento](base-de-conocimiento.md) a los hechos disponibles para deducir nuevas conclusiones.

## Estrategias de razonamiento

* **Encadenamiento hacia adelante:** parte de los hechos y aplica reglas hasta llegar a conclusiones.
* **Encadenamiento hacia atrás:** parte de una hipótesis y busca hechos que la confirmen.

## Ejemplo

Con los hechos `fiebre` y `tos`, y las reglas R1 "si hay fiebre y tos, entonces sospechar gripe" y R2 "si se sospecha gripe, entonces recomendar reposo", el motor aplica R1 y deduce `sospechar gripe`. Después aplica R2 sobre ese nuevo hecho y deduce `recomendar reposo`. Cada conclusión se convierte en un hecho más, y el proceso continúa mientras haya reglas aplicables.

## Ver también

* [Sistema experto](sistema-experto.md): el programa que contiene el motor.
* [Base de conocimiento](base-de-conocimiento.md): las reglas que el motor aplica.
