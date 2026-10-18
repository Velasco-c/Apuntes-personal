---
titulo: "Variable de entorno"
aliases: ["Variable de entorno", "variable de entorno", "variables de entorno", "environment variable"]
categoria: "fundamentos"
tags: ["concepto"]
---

# Variable de entorno

<!-- auto:categoria -->
Categoría: [Fundamentos](categoria.md)
<!-- /auto:categoria -->

Una **variable de entorno** es un valor de configuración que se define fuera del código de la aplicación, por ejemplo en el sistema operativo o en un archivo `.env`, y que el programa lee al ejecutarse. Se usa para datos que cambian entre entornos, como la dirección de un servidor, un puerto o una contraseña.

## Por qué se usan

Separan la configuración del código. El mismo programa puede ejecutarse en desarrollo, pruebas y producción cambiando solo sus valores. Además, evitan escribir credenciales en el código fuente, que puede compartirse o publicarse por error.

## Cómo se leen

En Node.js se leen desde `process.env`. Todos los valores llegan como texto, así que un número debe convertirse. Con [dotenv](../nodejs/dotenv.md) se cargan automáticamente desde un archivo `.env`.

```text
DB_HOST=localhost
DB_PORT=3306
```

```javascript
const puerto = Number(process.env.DB_PORT) || 3306;
```

## Buenas prácticas

El archivo `.env` con valores reales debe excluirse del control de versiones. Como alternativa, se publica una plantilla con los nombres de las variables y sin valores reales, por ejemplo `.env.example`.

## Ver también

* [dotenv](../nodejs/dotenv.md): biblioteca que carga el archivo `.env` en Node.js.
* [Controlador de base de datos](../acceso-a-datos/controlador-de-base-de-datos.md): recibe las credenciales de conexión que suelen guardarse en variables de entorno.
