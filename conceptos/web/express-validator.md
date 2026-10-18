---
titulo: "express-validator"
aliases: ["express-validator", "express validator"]
categoria: "web"
tags: ["concepto"]
---

# express-validator

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

**express-validator** es una biblioteca para Express que permite declarar reglas de [validación](../ingenieria/validacion-de-datos.md) y [sanitización](../ingenieria/sanitizacion-de-datos.md) sobre los datos de una petición, y consultar sus errores. Se usa como middleware dentro de la definición de una ruta.

## Ejemplo

```javascript
import { body, validationResult } from 'express-validator';

app.post('/user',
    body('email').isEmail().withMessage('Correo inválido').normalizeEmail(),
    (req, res) => {
        const errores = validationResult(req);

        if (!errores.isEmpty()) {
            return res.status(400).json({ errores: errores.array() });
        }

        res.status(201).json(req.body);
    }
);
```

## Sanitizadores frecuentes

Además de las validaciones, la biblioteca incluye sanitizadores que transforman el valor: `trim()` elimina espacios, `normalizeEmail()` normaliza un correo, `toInt()` convierte un texto en número y `escape()` escapa caracteres HTML. El orden importa: un sanitizador se aplica en la posición en que aparece en la cadena.

## Detener la cadena con bail()

Por defecto, express-validator ejecuta todas las reglas de un campo y reporta cada error. Si una regla posterior no tiene sentido cuando la anterior falla, se usa `bail()` para detener la cadena en el primer error.

## Ver también

* [Validación de datos](../ingenieria/validacion-de-datos.md): el concepto que la biblioteca implementa.
* [Middleware](middleware.md): la forma en que se integra en la ruta.
