---
titulo: "API"
aliases: ["API", "APIs", "interfaz de programación de aplicaciones"]
categoria: "web"
tags: ["concepto"]
---

# API

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Una **API** (*Application Programming Interface*, interfaz de programación de aplicaciones) es un conjunto de definiciones y protocolos que permiten que componentes de software se comuniquen entre sí. Especifica las operaciones disponibles, los datos que intercambian y el formato de las respuestas.

## Clasificación

* **Dependientes del lenguaje:** solo se usan con la sintaxis de un lenguaje concreto, como las bibliotecas estándar de ese lenguaje.
* **Independientes del lenguaje:** pueden usarse desde varios lenguajes, mediante servicios web o llamadas a procedimientos remotos (RPC).

## Protocolos y estilos frecuentes

| Protocolo | Primera versión | Formato | Fortaleza |
| --- | --- | --- | --- |
| SOAP | Finales de los 90 | XML | Amplia adopción y establecido |
| REST | 2000 | JSON, XML y otros | Formato de datos flexible |
| JSON-RPC | Mediados de los 2000 | JSON | Simplicidad de implementación |
| gRPC | 2015 | Protocol Buffers por defecto | Define cualquier tipo de función |
| GraphQL | 2015 | JSON | Estructuración flexible de datos |
| Thrift | 2007 | JSON o binario | Adaptable a muchos casos de uso |

REST es un estilo de arquitectura más que un protocolo estricto. Por eso suele implementarse sobre HTTP, con datos en JSON.

## Ver también

* [HTTP](http.md): el protocolo sobre el que se construyen la mayoría de las APIs web.
* [Modelo cliente-servidor](modelo-cliente-servidor.md): la arquitectura en la que una API opera.
