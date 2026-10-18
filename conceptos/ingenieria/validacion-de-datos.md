---
titulo: "Validación de datos"
aliases: ["Validación de datos", "validación de datos", "validar datos", "validación de entrada"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Validación de datos

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

La **validación de datos** es el proceso que comprueba que los datos recibidos cumplen las reglas esperadas antes de procesarlos o almacenarlos. Las reglas pueden exigir que un campo sea obligatorio, que tenga cierto tipo, formato o longitud, o que cumpla una condición del negocio.

## Tipos de regla

* **Obligatoriedad:** el campo debe tener un valor.
* **Tipo:** el valor debe ser un número, un texto o una fecha.
* **Formato:** el correo debe tener una estructura válida.
* **Rango o longitud:** la edad debe ser positiva, o el nombre no debe superar cierta cantidad de caracteres.
* **Negocio:** por ejemplo, un correo que está bloqueado no puede registrarse.

## Dónde validar

Los datos deben validarse en el servidor, aunque también puedan validarse en el cliente. La validación del cliente mejora la experiencia de uso, pero cualquiera puede enviar peticiones sin pasar por ella.

## Ver también

* [Sanitización de datos](sanitizacion-de-datos.md): transforma los datos antes de validarlos.
* [express-validator](../web/express-validator.md): una biblioteca que declara estas reglas en Express.
