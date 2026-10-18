---
titulo: "Escalabilidad"
aliases: ["Escalabilidad", "escalabilidad", "escalable", "escalar"]
categoria: "ingenieria"
tags: ["concepto"]
---

# Escalabilidad

<!-- auto:categoria -->
Categoría: [Ingeniería de software](categoria.md)
<!-- /auto:categoria -->

La **escalabilidad** es la capacidad de un sistema para atender más carga, como más usuarios, más peticiones o más datos, sin perder rendimiento de forma inaceptable.

## Tipos de escalado

* **Vertical:** aumentar los recursos de una misma máquina, con más memoria o más procesador. Es sencillo, pero tiene un límite físico y económico.
* **Horizontal:** añadir más máquinas que compartan la carga. Requiere que la aplicación pueda distribuirse, por ejemplo guardando su estado fuera del proceso.

## Factores que la limitan

* Consultas lentas o tablas sin [índices](../bases-de-datos/estructura/indice-bd.md).
* Conexiones a la base de datos que se agotan. Un [pool de conexiones](../acceso-a-datos/pool-de-conexiones.md) ayuda a administrarlas.
* Estado guardado en memoria local, que impide ejecutar varias instancias del mismo servicio.

## Ver también

* [Persistencia de datos](../fundamentos/persistencia.md): cómo el estado se guarda fuera del proceso.
* [Pool de conexiones](../acceso-a-datos/pool-de-conexiones.md): una de las piezas para escalar el acceso a datos.
