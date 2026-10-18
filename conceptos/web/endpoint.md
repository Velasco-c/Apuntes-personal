---
titulo: "Endpoint"
aliases: ["Endpoint", "endpoint", "endpoints"]
categoria: "web"
tags: ["concepto"]
---

# Endpoint

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **endpoint** es una combinación de un método HTTP y una ruta que el servidor atiende, por ejemplo `GET /campus`. Cada endpoint cumple una función específica dentro de la API.

## Ejemplo en Express

```javascript
app.get('/campus', (req, res) => {
    res.json({ mensaje: 'Hola desarrollador' });
});
```

## Diseño

Un buen diseño usa rutas que describen recursos, como `/productos` o `/productos/3`, y deja que el método HTTP indique la acción. Así, `DELETE /productos/3` es más claro que `GET /eliminarProducto?id=3`.

## Respuestas de un endpoint

Un endpoint debe responder siempre con un código de estado adecuado y un cuerpo con formato consistente. Por ejemplo, una lista devuelve `200` con un arreglo, una creación devuelve `201` con el recurso creado, y un recurso inexistente devuelve `404` con un mensaje de error. Cuando la API evoluciona de forma incompatible, se suele versionar en la ruta, como `/api/v1/productos`.

## Ver también

* [CRUD](../sql/crud.md): las operaciones que suelen exponerse como endpoints.
* [Parámetro de ruta](parametro-de-ruta.md): la forma de capturar valores variables en la ruta.
