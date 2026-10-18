---
titulo: "Express"
aliases: ["Express", "Express.js", "expressjs"]
categoria: "web"
tags: ["concepto"]
---

# Express

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

**Express** es un marco de trabajo minimalista y flexible para Node.js que simplifica la creación de aplicaciones web y APIs. Proporciona las herramientas esenciales, como rutas, middlewares y el manejo de peticiones y respuestas, y deja el resto a las necesidades de cada proyecto.

## Ejemplo mínimo

```javascript
import express from 'express';

const app = express();

app.get('/', (req, res) => {
    res.send('Hello World');
});

app.listen(3000);
```

## Piezas principales

* **Rutas:** [endpoints](endpoint.md) definidos con métodos como `get` o `post`.
* **Middlewares:** funciones que procesan cada petición. Ver [middleware](middleware.md).
* **Routers:** agrupación de rutas por recurso. Ver [router](router.md).

## Cuándo usar Express

Express es adecuado para APIs y aplicaciones web con lógica personalizada, porque deja al desarrollador elegir cada pieza. Su minimalismo también significa que funciones como la validación, la autenticación o la documentación se añaden con bibliotecas. En Express 5, los errores de funciones `async` se envían automáticamente al manejador de errores, algo que en versiones anteriores debía hacerse con `next(error)`.

## Ver también

* [Node.js](../nodejs/nodejs.md): el entorno sobre el que se ejecuta Express.
* [express-validator](express-validator.md): una biblioteca de validación que se integra con Express.
