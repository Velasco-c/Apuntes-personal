---
titulo: "Model Context Protocol (MCP)"
aliases: ["Model Context Protocol (MCP)", "MCP", "Model Context Protocol"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Model Context Protocol (MCP)

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

El **Model Context Protocol** (MCP) es un protocolo abierto que estandariza la forma en que un modelo de IA se conecta con herramientas y fuentes de datos externas. Un mismo servidor MCP puede usarse desde distintas aplicaciones de IA.

## Componentes

* **Cliente:** la aplicación de IA que usa las herramientas.
* **Servidor:** expone herramientas, recursos o instrucciones, como el acceso a una base de datos o a un sistema de archivos.

## Relación con function calling

El [function calling](function-calling.md) es el mecanismo por el que el modelo solicita una acción. MCP define cómo se descubren y se conectan esas herramientas de forma estándar.

## Ejemplo de uso

Un servidor MCP puede exponer una herramienta de solo lectura para consultar el catálogo de productos de una base de datos. Cuando el usuario pregunta por el precio de un teclado, el modelo solicita esa herramienta con el código del producto, el servidor ejecuta una consulta preparada y devuelve el resultado. El modelo responde con un dato actual en lugar de inventarlo.

## Ver también

* [Function calling](function-calling.md): el mecanismo que MCP estandariza.
* [LLM](llm.md): el modelo que se conecta a las herramientas.
