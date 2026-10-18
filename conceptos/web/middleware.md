---
titulo: "Middleware"
aliases: ["Middleware", "middleware", "middlewares"]
categoria: "web"
tags: ["concepto"]
---

# Middleware

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **middleware** es una función que recibe el objeto de solicitud (`req`), el de respuesta (`res`) y la función `next`, y forma parte de una pila que se ejecuta en secuencia cuando llega una petición. Puede procesar la petición, modificar la respuesta, validar datos o terminar la petición.

## Cómo funciona

Cada middleware realiza su tarea y, si no termina la petición, llama a `next()` para pasar el control al siguiente. Si no llama a `next()` ni envía una respuesta, la petición queda sin terminar.

```javascript
app.use((req, res, next) => {
    console.log(req.method, req.url);
    next();
});
```

## Usos habituales

Registrar peticiones, interpretar el cuerpo JSON, verificar la autenticación, validar datos, comprimir respuestas y manejar errores.

## Ver también

* [Router](router.md): agrupa rutas que se apoyan en los mismos middlewares.
* [Manejo centralizado de errores](../ingenieria/manejo-centralizado-de-errores.md): un middleware especial con cuatro parámetros.
