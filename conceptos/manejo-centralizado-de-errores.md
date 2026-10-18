---
titulo: "Manejo centralizado de errores"
aliases: ["Manejo centralizado de errores", "manejo centralizado de errores", "errorHandler"]
tags: ["concepto"]
---

# Manejo centralizado de errores

Patrón en el que los errores de la aplicación se pasan a un único manejador de [Express](express.md) con cuatro parámetros, que devuelve todas las respuestas de error con el mismo formato.

<!-- auto:backlinks -->
## Dónde aparece

- [DTO y validación de datos en Node.js con Express](../express/04-dto-y-validacion-express.md) · Express · 2 menciones

## Conceptos cercanos

- [DTO (Data Transfer Object)](dto.md): Patrón de diseño que usa un objeto simple para transportar datos entre capas o componentes de una aplicación, sin lógica de negocio.
- [Validación de datos](validacion-de-datos.md): Proceso que comprueba que los datos recibidos cumplen reglas de obligatoriedad, tipo, formato y longitud antes de procesarlos o almacenarlos.
- [Node.js](nodejs.md): Entorno de ejecución que permite ejecutar JavaScript fuera del navegador.
- [Express.js](express.md): Marco de trabajo minimalista para Node.js que simplifica la creación de aplicaciones web y APIs, con herramientas para definir rutas, middlewares y manejar peticiones y respuestas…
- [API (Interfaz de programación de aplicaciones)](api.md): Conjunto de definiciones y protocolos que permiten que componentes de software se comuniquen e integren, especificando las rutinas, estructuras de datos y variables que otros progr…
- [express-validator](express-validator.md): Biblioteca de validación para Express que se usa como middleware.
<!-- /auto:backlinks -->
