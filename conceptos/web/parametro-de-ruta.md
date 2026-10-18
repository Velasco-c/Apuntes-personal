---
titulo: "Parámetro de ruta"
aliases: ["Parámetro de ruta", "parámetro de ruta", "parámetros de ruta", "params"]
categoria: "web"
tags: ["concepto"]
---

# Parámetro de ruta

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **parámetro de ruta** es una parte variable de una URL que el servidor captura y entrega a la aplicación. Se define en la ruta con dos puntos seguidos de un nombre, como `:idCamper`, y su valor real se consulta en `req.params`.

## Ejemplo en Express

```javascript
app.get('/campus/:idCamper', (req, res) => {
    res.json({ idCamper: req.params.idCamper });
});
```

Con `GET /campus/42`, el valor de `req.params.idCamper` es `"42"`.

## Puntos a considerar

* El valor siempre llega como texto. Si se necesita un número, debe convertirse, por ejemplo con `Number()`.
* No es lo mismo que un parámetro de consulta (`?clave=valor`), que se lee en `req.query`.

## Validar el parámetro

Un parámetro de ruta siempre llega como texto, así que conviene validarlo antes de usarlo. Con express-validator se puede declarar una regla sobre el parámetro, por ejemplo `param('id').isInt({ min: 1 })`. Así, una petición como `GET /productos/abc` se rechaza con `400` sin llegar a la consulta a la base de datos.

## Ver también

* [Endpoint](endpoint.md): la ruta en la que se define el parámetro.
* [Encabezado HTTP](encabezado-http.md): otra forma de recibir datos desde el cliente.
