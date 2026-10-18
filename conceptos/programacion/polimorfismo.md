---
titulo: "Polimorfismo"
aliases: ["Polimorfismo", "polimorfismo"]
categoria: "programacion"
tags: ["concepto"]
---

# Polimorfismo

<!-- auto:categoria -->
Categoría: [Programación orientada a objetos](categoria.md)
<!-- /auto:categoria -->

El **polimorfismo** es la capacidad de tratar objetos de distinto tipo mediante una misma interfaz, de modo que cada uno responde a su manera a la misma operación. Permite escribir código genérico que funciona con cualquier objeto que cumpla el contrato esperado.

## Ejemplo

```javascript
// Asumiendo que Circulo y Rectangulo tienen un método area()
const figuras = [new Circulo(2), new Rectangulo(3, 4)];

for (const figura of figuras) {
    console.log(figura.area());
}
```

Cada figura calcula su área con su propia fórmula. El bucle no necesita saber de qué tipo es cada objeto.

## Formas de lograrlo

El polimorfismo puede implementarse por herencia, sobrescribiendo métodos, o por una interfaz común. JavaScript no tiene interfaces formales, así que el contrato se define por convención: si un objeto tiene el método esperado, puede usarse.

## Sobrescritura de métodos

En el ejemplo de herencia, `Perro` sobrescribe `hablar`. Si se recorre una lista que contiene objetos de `Animal` y de `Perro`, la llamada `hablar()` produce "Sonido genérico" para los primeros y "Guau" para los segundos, sin que el código del bucle cambie. Esa es la base práctica del polimorfismo: el comportamiento depende del objeto concreto, no del tipo declarado en la variable.

## Ver también

* [Herencia](herencia.md): una de las formas de lograr polimorfismo.
* [Programación orientada a objetos](poo.md): el paradigma al que pertenece.
