---
titulo: "Router"
aliases: ["Router", "router", "routers", "enrutador"]
categoria: "web"
tags: ["concepto"]
---

# Router

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

Un **router** es un objeto que agrupa rutas relacionadas en un módulo independiente. En Express, cada recurso de la API puede tener su propio router con sus rutas y controladores, y luego se monta en la aplicación principal con un prefijo.

## Ejemplo

```javascript
// routes/estudiante.route.js
import { Router } from 'express';

const estudianteRouter = Router();

estudianteRouter.get('/', (req, res) => {
    res.json([]);
});

export default estudianteRouter;
```

```javascript
// app.js
app.use('/estudiantes', estudianteRouter);
```

Al montarse con el prefijo `/estudiantes`, la ruta `/` del router responde en `/estudiantes`.

## Ventajas

Separa la aplicación por recursos, facilita el trabajo en equipo y permite reutilizar un módulo en otras aplicaciones.

## Routers anidados

Un router puede montar otro router en una ruta de su propio prefijo. Por ejemplo, un router de `/pedidos` puede montar un router de `/detalles`, de modo que las rutas quedan como `/pedidos/:id/detalles`. Conviene anidar solo uno o dos niveles, porque los niveles profundos hacen difícil seguir el recorrido de una petición.

## Ver también

* [Endpoint](endpoint.md): las rutas que agrupa el router.
* [Express](express.md): el marco de trabajo que implementa los routers.
