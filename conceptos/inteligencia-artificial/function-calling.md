---
titulo: "Function calling"
aliases: ["Function calling", "function calling", "llamada a funciones", "tool calling"]
categoria: "inteligencia-artificial"
tags: ["concepto"]
---

# Function calling

<!-- auto:categoria -->
Categoría: [Inteligencia artificial](categoria.md)
<!-- /auto:categoria -->

El **function calling** es un mecanismo por el que un modelo de lenguaje solicita ejecutar una función definida por la aplicación, con argumentos estructurados, y después usa el resultado en su respuesta. El modelo no ejecuta el código: decide qué función llamar y con qué datos, y la aplicación la ejecuta.

## Flujo

1. La aplicación describe las funciones disponibles, con su nombre, sus parámetros y su propósito.
2. El modelo decide llamar a una función y genera sus argumentos en formato estructurado, normalmente JSON.
3. La aplicación ejecuta la función y devuelve el resultado al modelo.
4. El modelo redacta la respuesta final con esa información.

## Ejemplo

Una función `consultarStock(codigo)` permite al modelo responder con datos reales del inventario, en lugar de inventarlos.

## Ver también

* [MCP](mcp.md): un protocolo que estandariza estas herramientas.
* [Alucinación](alucinacion.md): el riesgo que se reduce al consultar datos reales.
