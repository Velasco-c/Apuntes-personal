---
titulo: "nodemon"
aliases: ["nodemon"]
categoria: "nodejs"
tags: ["concepto"]
---

# nodemon

<!-- auto:categoria -->
Categoría: [Node.js y herramientas](categoria.md)
<!-- /auto:categoria -->

**nodemon** es una herramienta de desarrollo que observa los archivos de un proyecto Node.js y reinicia el servidor automáticamente cuando detecta cambios. Evita detener y volver a ejecutar el servidor después de cada modificación.

## Qué observa

Por defecto observa archivos JavaScript y JSON. Puede configurarse para observar otras extensiones o para ignorar carpetas, como `node_modules`.

## Uso

```bash
npm install --save-dev nodemon
```

```json
"scripts": {
    "dev": "nodemon app.js"
}
```

Después se ejecuta con `npm run dev`.

## Limitación

Es una herramienta de desarrollo. En producción el servidor se ejecuta directamente con `node`, sin reinicios automáticos.

## Configuración con nodemon.json

Para personalizar el comportamiento, se crea un archivo `nodemon.json` en la raíz del proyecto:

```json
{
    "ignore": ["node_modules", "public/*"],
    "ext": "js,json"
}
```

`ignore` indica las rutas que no deben observarse, y `ext` las extensiones que sí deben vigilarse.

## Ver también

* [npm](npm.md): el gestor que instala nodemon y ejecuta sus scripts.
* [Express](../web/express.md): el tipo de servidor que suele desarrollarse con nodemon.
