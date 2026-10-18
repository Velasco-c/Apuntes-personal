---
titulo: "Base de conocimiento"
aliases: ["Base de conocimiento", "base de conocimiento", "bases de conocimiento"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Base de conocimiento

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

Una **base de conocimiento** es un conjunto estructurado de hechos y reglas que un [sistema experto](sistema-experto.md) usa para razonar. A diferencia de una [base de datos](../bases-de-datos/base-de-datos.md), que guarda datos, la base de conocimiento guarda relaciones y reglas que permiten deducir nuevas conclusiones.

## Ejemplo

* Hecho: "el paciente tiene fiebre".
* Regla: "si hay fiebre y tos, sospechar gripe".

El [motor de inferencia](motor-de-inferencia.md) puede concluir "sospechar gripe" sin que esa conclusión esté escrita de antemano.

## Cómo se construye

La base de conocimiento se construye con la colaboración de especialistas del dominio y de un ingeniero del conocimiento, que traduce su experiencia a reglas explícitas. Un proceso típico identifica los hechos relevantes, define las reglas de la forma "si ocurre X y Y, entonces Z", y después prueba el sistema con casos reales para corregir las reglas incorrectas o incompletas.

## Ver también

* [Sistema experto](sistema-experto.md): el programa que usa la base de conocimiento.
* [Motor de inferencia](motor-de-inferencia.md): el componente que aplica las reglas.
