---
titulo: "Modelo de lenguaje de gran escala (LLM)"
aliases: ["Modelo de lenguaje de gran escala (LLM)", "LLM", "modelo de lenguaje de gran escala", "modelo de lenguaje", "modelos de lenguaje"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Modelo de lenguaje de gran escala (LLM)

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

Un **modelo de lenguaje de gran escala** (LLM, *Large Language Model*) es una [red neuronal](red-neuronal.md) entrenada con grandes volúmenes de texto para predecir el siguiente fragmento de texto. De esa tarea surgen capacidades como responder preguntas, resumir, traducir o escribir código.

## Cómo se usa

El modelo recibe un texto de entrada, llamado [prompt](prompt.md), y genera una continuación. Puede ampliarse con herramientas externas mediante [function calling](function-calling.md) o el protocolo [MCP](mcp.md).

## Limitaciones

* Puede producir [alucinaciones](alucinacion.md): respuestas plausibles pero falsas.
* Su conocimiento proviene del entrenamiento y tiene una fecha de corte, salvo que se conecte a fuentes actuales.

## Ver también

* [Red neuronal](red-neuronal.md): la arquitectura en la que se basa.
* [Alucinación](alucinacion.md): uno de los riesgos más importantes.
