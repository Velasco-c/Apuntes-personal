---
titulo: "Manejo centralizado de errores"
aliases: ["Manejo centralizado de errores", "manejo centralizado de errores", "errorHandler"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Manejo centralizado de errores

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

El **manejo centralizado de errores** es un patrón en el que todos los errores de la aplicación se entregan a un único manejador, que decide la respuesta que se envía. Así, las respuestas de error tienen siempre el mismo formato y las rutas no repiten la misma lógica.

## Cómo funciona en Express

El manejador es un [middleware](../web/middleware.md) con cuatro parámetros: `(err, req, res, next)`. Las rutas llaman a `next(error)` cuando algo falla, y el manejador responde con el código adecuado.

```javascript
app.use((err, req, res, next) => {
    res.status(err.statusCode || 500).json({
        message: err.message || 'Error interno del servidor'
    });
});
```

## Ventajas

* Formato uniforme en todas las respuestas de error.
* Separación entre la lógica de negocio y la forma de responder.
* Un único lugar donde registrar los errores.

## Ver también

* [Middleware](../web/middleware.md): la pieza que implementa el manejador.
* [Código de estado HTTP](../web/codigo-de-estado-http.md): los códigos que el manejador devuelve.
