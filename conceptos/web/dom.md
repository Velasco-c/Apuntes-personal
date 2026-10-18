---
titulo: "DOM (Document Object Model)"
aliases: ["DOM (Document Object Model)", "DOM", "Document Object Model"]
categoria: "web"
tags: ["concepto"]
---

# DOM (Document Object Model)

<!-- auto:categoria -->
Categoría: [Web y APIs](categoria.md)
<!-- /auto:categoria -->

El **DOM** (*Document Object Model*) es la representación en forma de árbol de un documento HTML. Cada etiqueta se convierte en un nodo que JavaScript puede leer, modificar, crear o eliminar, lo que permite cambiar una página sin recargarla.

## Ejemplo

```html
<p id="mensaje">Hola</p>
```

```javascript
document.getElementById('mensaje').textContent = 'Bienvenido';
```

## Relación con Node.js

El DOM existe en el navegador. Node.js no tiene DOM porque no renderiza páginas: su trabajo es ejecutar la lógica del servidor.

## Nodos y eventos

Los elementos se localizan con `querySelector` o `getElementById`. Para reaccionar a acciones del usuario se registran eventos con `addEventListener`:

```javascript
const boton = document.querySelector('#enviar');

boton.addEventListener('click', () => {
    console.log('Botón pulsado');
});
```

Cada modificación del DOM puede provocar un nuevo cálculo de la página, así que conviene agrupar los cambios en lugar de hacerlos uno por uno.

## Ver también

* [Modelo cliente-servidor](modelo-cliente-servidor.md): el DOM pertenece al lado del cliente.
* [JSON](../formatos/json.md): un formato que el cliente suele recibir del servidor para actualizar el DOM.
