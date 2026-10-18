---
titulo: "Encabezado HTTP"
aliases: ["Encabezado HTTP", "encabezado HTTP", "encabezados HTTP", "headers"]
categoria: "web"
tags: ["concepto"]
---

# Encabezado HTTP

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **encabezado HTTP** (*header*) es un metadato que se envía junto con una petición o una respuesta. Describe aspectos como el tipo de contenido, la codificación, las cookies o la autenticación, sin formar parte de los datos del cuerpo.

## Ejemplos frecuentes

* `Content-Type: application/json`: indica que el cuerpo está en formato JSON.
* `Authorization`: transporta credenciales o tokens.
* `Cookie`: envía al servidor las cookies que guarda el cliente.

## En Express

Los encabezados de la petición se leen desde `req.headers`. Node.js guarda sus nombres en minúsculas, así que `req.headers['content-type']` funciona aunque el cliente los envíe con otras mayúsculas.

```javascript
const tipo = req.headers['content-type'];
```

## Advertencia

Un encabezado lo envía el cliente y puede falsificarse. No debe usarse solo para decisiones de seguridad, como saber si un usuario es administrador.

## Ver también

* [HTTP](http.md): el protocolo que define los encabezados.
* [Parámetro de ruta](parametro-de-ruta.md): otra forma de recibir información desde la petición.
