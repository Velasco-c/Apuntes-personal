---
titulo: "Alucinación"
aliases: ["Alucinación", "alucinación", "alucinaciones", "alucinar"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Alucinación

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

Una **alucinación** en un modelo de lenguaje es una respuesta que suena plausible, pero es falsa o no está respaldada por fuentes. El modelo genera texto coherente sin verificar si el contenido corresponde a la realidad.

## Causas

* El modelo predice la continuación más probable, no necesariamente la verdad.
* Faltan datos sobre el tema en su entrenamiento.
* La pregunta pide una precisión que el modelo no puede tener, como una cita textual exacta.

## Cómo reducirlas

* Incluir en el [prompt](prompt.md) el contexto verificado.
* Pedir fuentes y comprobarlas.
* Usar herramientas externas para consultar datos actuales, mediante [function calling](function-calling.md).

## Ejemplo

Se le pide a un modelo un ejemplo de una función de una biblioteca. El modelo puede devolver un nombre de función que no existe en esa versión, con una firma plausible pero incorrecta. El código parece correcto, pero falla al ejecutarse. Por eso el código generado debe probarse antes de usarse.

## Ver también

* [LLM](llm.md): el tipo de modelo donde ocurre el fenómeno.
* [Prompt](prompt.md): la principal forma de reducirlo en la práctica.
