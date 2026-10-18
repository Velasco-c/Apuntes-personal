---
titulo: "DTO (Data Transfer Object)"
aliases: ["DTO (Data Transfer Object)", "DTO", "DTOs", "Data Transfer Object", "objeto de transferencia de datos"]
categoria: "ingenieria"
tags: ["concepto"]
---

# DTO (Data Transfer Object)

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

Un **DTO** (*Data Transfer Object*, objeto de transferencia de datos) es un patrón de diseño que define un objeto simple para transportar datos entre capas o componentes de una aplicación. Contiene campos y, normalmente, métodos de acceso, pero no lógica de negocio.

## Para qué sirve

* **Dar una estructura clara** a los datos que entran o salen de una capa.
* **Limitar lo que se expone:** un DTO de salida puede omitir campos sensibles, como una contraseña.
* **Desacoplar capas:** la capa de presentación, la de negocio y la de acceso a datos pueden cambiar sin romper a las demás.
* **Facilitar el mantenimiento:** un cambio en la estructura de los datos se concentra en un solo lugar.

## Ejemplo

```javascript
function crearUsuarioDTO(nombre, correo, edad) {
    return { nombre, correo, edad };
}
```

Un DTO de entrada describe los datos que llegan en una petición, y un DTO de salida describe lo que la API devuelve. Ambos pueden ser distintos a la entidad que se guarda en la base de datos.

## Ver también

* [Validación de datos](validacion-de-datos.md): comprueba los datos antes de construir el DTO.
* [Patrón de diseño](patron-de-diseno.md): la categoría general a la que pertenece.
