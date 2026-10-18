---
titulo: "Código de estado HTTP"
aliases: ["Código de estado HTTP", "código de estado HTTP", "códigos de estado", "status code"]
categoria: "web"
tags: ["concepto"]
---

# Código de estado HTTP

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **código de estado HTTP** es un número de tres dígitos que el servidor devuelve para indicar el resultado de una solicitud. El primer dígito indica la clase de respuesta.

| Clase | Significado | Ejemplos |
| --- | --- | --- |
| 1xx | Informativa: la solicitud se recibió y continúa | 100 |
| 2xx | Éxito | 200, 201 |
| 3xx | Redirección: se necesita otra acción | 301, 302 |
| 4xx | Error del cliente: la solicitud es incorrecta o no puede cumplirse | 400, 401, 403, 404 |
| 5xx | Error del servidor: no pudo cumplir una solicitud válida | 500, 502, 503 |

## Códigos frecuentes en una API

* `200` OK: la petición se procesó y hay datos que devolver.
* `201` Created: se creó un recurso nuevo.
* `400` Bad Request: faltan datos o tienen un formato incorrecto.
* `401` Unauthorized: falta la identificación del usuario.
* `403` Forbidden: el usuario está identificado, pero no tiene permiso.
* `404` Not Found: el recurso solicitado no existe.
* `500` Internal Server Error: ocurrió un error inesperado en el servidor.

## Ver también

* [HTTP](http.md): el protocolo que transporta el código.
* [Manejo centralizado de errores](../ingenieria/manejo-centralizado-de-errores.md): cómo asignar el código a cada error.
