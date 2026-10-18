---
titulo: "Herencia"
aliases: ["Herencia", "herencia"]
categoria: "programacion"
tags: ["concepto"]
---

# Herencia

<!-- auto:categoria -->
Categoría: [Programación orientada a objetos](categoria.md)
<!-- /auto:categoria -->

La **herencia** es un mecanismo por el que una clase recibe los atributos y métodos de otra, llamada clase padre o superclase, y puede extenderlos o modificarlos. Permite reutilizar código común en clases más especializadas.

## Ejemplo

```javascript
class Animal {
    hablar() {
        return 'Sonido genérico';
    }
}

class Perro extends Animal {
    hablar() {
        return 'Guau';
    }
}
```

`Perro` reutiliza la estructura de `Animal` y sobrescribe el método `hablar`.

## Cuidados

Una jerarquía de herencia profunda acopla las clases entre sí: un cambio en la clase padre puede afectar a todas sus hijas. Cuando solo se necesita reutilizar un comportamiento, suele ser preferible la **composición**, en la que una clase usa otra como componente.

## Llamadas a super

Cuando una clase hija define su propio constructor, debe llamar a `super()` para ejecutar el constructor de la clase padre. Sin esa llamada, JavaScript lanza un error al intentar usar `this`. Dentro de un método sobrescrito, `super.metodo()` permite reutilizar el comportamiento del padre y añadir solo lo que cambia.

## Ver también

* [Polimorfismo](polimorfismo.md): lo que se consigue al sobrescribir métodos heredados.
* [Principios SOLID](../ingenieria/solid.md): el principio de sustitución de Liskov define cuándo una herencia es correcta.
