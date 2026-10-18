---
titulo: "HTTP"
aliases: ["HTTP", "protocolo HTTP"]
categoria: "web"
tags: ["concepto"]
---

# HTTP

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

**HTTP** (*Hypertext Transfer Protocol*) es el protocolo de comunicación de la web. El cliente, como un navegador o una aplicación, envía una solicitud con un método y una ruta, y el servidor responde con un [código de estado](codigo-de-estado-http.md), encabezados y, si corresponde, un cuerpo.

## Partes de una solicitud

* **Método:** indica la acción, como `GET`, `POST`, `PUT`, `PATCH` o `DELETE`.
* **Ruta:** identifica el recurso, como `/productos/3`.
* **Encabezados:** metadatos, como el tipo de contenido o la autenticación.
* **Cuerpo:** datos enviados, por ejemplo un objeto JSON.

## Partes de una respuesta

Código de estado, encabezados y cuerpo, normalmente en formato JSON o HTML.

## Ejemplo

```bash
curl -i http://localhost:3000/productos
```

La opción `-i` muestra los encabezados y el código de estado junto con la respuesta.

## Ver también

* [Encabezado HTTP](encabezado-http.md): los metadatos que acompañan cada mensaje.
* [Endpoint](endpoint.md): la combinación de método y ruta que atiende el servidor.
