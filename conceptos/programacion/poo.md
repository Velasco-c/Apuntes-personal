---
titulo: "Programación orientada a objetos"
aliases: ["Programación orientada a objetos", "programación orientada a objetos", "POO", "OOP"]
categoria: "programacion"
tags: ["concepto"]
---

# Programación orientada a objetos

<!-- auto:categoria -->
Categoría: [Programación orientada a objetos](categoria.md)
<!-- /auto:categoria -->

La **programación orientada a objetos** (POO) es un paradigma que organiza el código en objetos. Un objeto combina datos (propiedades) y comportamiento (métodos), y normalmente se crea a partir de una **clase**, que actúa como plantilla.

## Pilares

* **Encapsulamiento:** los datos internos se protegen y se acceden mediante métodos o getters.
* **Abstracción:** el objeto expone lo necesario y oculta el detalle de su funcionamiento.
* **Herencia:** una clase reutiliza y extiende a otra, como se explica en [herencia](herencia.md).
* **Polimorfismo:** objetos distintos responden a la misma operación, como se explica en [polimorfismo](polimorfismo.md).

## Ejemplo en JavaScript

```javascript
class Producto {
    #precio;

    constructor(nombre, precio) {
        this.nombre = nombre;
        this.#precio = precio;
    }

    get precio() {
        return this.#precio;
    }
}

const teclado = new Producto('Teclado', 350);
console.log(teclado.precio); // 350
```

## Clase frente a objeto

Una **clase** es la definición general, como un molde. Un **objeto** es una instancia concreta creada a partir de esa clase. La clase `Producto` define que todo producto tiene nombre y precio; `new Producto('Teclado', 350)` crea un objeto con valores específicos. Una misma clase puede generar muchos objetos independientes entre sí.

## Ver también

* [Herencia](herencia.md): una de las relaciones entre clases.
* [Principios SOLID](../ingenieria/solid.md): criterios para diseñar clases que se mantengan bien con el tiempo.
