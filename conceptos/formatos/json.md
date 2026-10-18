---
titulo: "JSON"
aliases: ["JSON", "JSONB"]
categoria: "formatos"
tags: ["concepto"]
---

# JSON

<!-- auto:categoria -->
Categoría: [Formatos de datos](categoria.md)
<!-- /auto:categoria -->

**JSON** (*JavaScript Object Notation*) es un formato de texto ligero para representar datos estructurados mediante pares clave-valor y arreglos. Es fácil de leer para las personas y de procesar para las máquinas, y es el formato más usado en las APIs web.

## Tipos de valor

* Texto entre comillas dobles, números, booleanos (`true` y `false`) y `null`.
* Objetos (`{ }`) y arreglos (`[ ]`), que pueden anidarse.

## Ejemplo

```json
{
  "id": 1,
  "nombre": "Teclado mecánico",
  "activo": true,
  "etiquetas": ["periférico", "usb"]
}
```

## Notas

JSON no admite comentarios ni valores como `undefined`. PostgreSQL ofrece el tipo `JSONB`, que guarda el documento en formato binario y permite consultar sus campos.

## Errores comunes

Un JSON mal formado produce un error de análisis en la aplicación. Los errores más frecuentes son usar comillas simples en lugar de dobles, dejar una coma después del último elemento, o escribir claves sin comillas. `JSON.parse` lanza un error en cualquiera de estos casos, por lo que las respuestas de una API deben validarse antes de usarse.

## Ver también

* [API](../web/api.md): el formato habitual de sus respuestas.
* [XML](xml.md): un formato alternativo más antiguo y más verboso.
