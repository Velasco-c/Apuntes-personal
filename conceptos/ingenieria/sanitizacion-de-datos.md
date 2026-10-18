---
titulo: "Sanitización de datos"
aliases: ["Sanitización de datos", "sanitización de datos", "sanitizar", "sanitización"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Sanitización de datos

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

La **sanitización de datos** es el proceso que limpia o transforma los datos de entrada para dejarlos en una forma uniforme y segura. Por ejemplo, elimina espacios sobrantes, normaliza un correo electrónico o convierte un texto numérico en un número.

## Diferencia con la validación

La [validación](validacion-de-datos.md) decide si un dato es aceptable. La sanitización lo modifica para que pueda serlo. Un valor puede sanearse y, aun así, rechazarse si no cumple las reglas.

## Ejemplos

| Entrada | Transformación | Resultado |
| --- | --- | --- |
| `"  Ana  "` | Eliminar espacios | `"Ana"` |
| `"ANA@Example.com"` | Normalizar el correo | `"ana@example.com"` |
| `"30"` | Convertir a número | `30` |

## Límite

Sanear la entrada no protege la salida. Si un dato se muestra en una página HTML, debe escaparse en ese momento para evitar ataques de tipo XSS.

## Ver también

* [Validación de datos](validacion-de-datos.md): la decisión de aceptar o rechazar un dato.
* [express-validator](../web/express-validator.md): una biblioteca que incluye sanitizadores.
