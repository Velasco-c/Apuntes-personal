---
titulo: "Testing automatizado"
aliases: ["Testing automatizado", "testing automatizado", "pruebas automatizadas", "pruebas unitarias"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Testing automatizado

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

El **testing automatizado** consiste en verificar el comportamiento del software mediante pruebas que se ejecutan de forma automática y repetible. Permite detectar errores cada vez que se cambia el código, sin depender de revisar cada función a mano.

## Tipos de prueba

* **Unitarias:** prueban una función o una clase de forma aislada.
* **De integración:** comprueban que varios componentes funcionan juntos, por ejemplo una ruta con su base de datos.
* **End-to-end:** recorren la aplicación como lo haría un usuario real.

## Ejemplo con el módulo de pruebas de Node.js

```javascript
import { test } from 'node:test';
import assert from 'node:assert';

function sumar(a, b) {
    return a + b;
}

test('sumar devuelve la suma de dos números', () => {
    assert.strictEqual(sumar(2, 3), 5);
});
```

## Forma de las pruebas

Una estrategia común es la **pirámide de pruebas**: muchas pruebas unitarias, que son rápidas y baratas; algunas pruebas de integración, que son más lentas; y pocas pruebas end-to-end, que son las más costosas de mantener. Una prueba debe ser independiente de las demás y producir el mismo resultado en cada ejecución.

## Ver también

* [Principios SOLID](solid.md): el código con responsabilidades separadas es más fácil de probar.
* [Validación de datos](validacion-de-datos.md): una de las reglas más útiles de verificar con pruebas.
