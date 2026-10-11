---
titulo: "Apuntes de aprendizaje autodidacta"
tags: ["portada"]
---

# Apuntes de aprendizaje autodidacta

Apuntes de estudio sobre bases de datos (SQL, MySQL y PostgreSQL), JavaScript con Node.js e inteligencia artificial. Están ordenados para estudiarlos en secuencia y para encontrar un tema en segundos.

No es un curso oficial. Es un registro vivo que se corrige y se amplía con el tiempo.

## Cómo buscar un tema

1. Abre [cerebro/inicio.md](cerebro/inicio.md). Es un índice único con todos los conceptos y todas las secciones de las lecciones.
2. Pulsa `Ctrl+F` y escribe el tema, en español o en inglés (por ejemplo `trigger`, `foreign key`, `SOLID`, `window function`).
3. Haz clic en el enlace: te lleva directamente a la sección.

Si ya sabes en qué área está, abre su carpeta, o usa la búsqueda global de tu editor (`Ctrl+Shift+F`).

## Estructura

<!-- auto:areas -->
1. [Bases de datos](bases-de-datos/indice.md): 5 lecciones
2. [MySQL](mysql/indice.md): 10 lecciones
3. [PostgreSQL](postgresql/indice.md): 7 lecciones
4. [Node.js](nodejs/indice.md): 8 lecciones
5. [Inteligencia artificial](inteligencia-artificial/indice.md): 9 lecciones
<!-- /auto:areas -->

- `conceptos/`: una nota corta por concepto, con enlaces a las lecciones donde aparece.
- `cerebro/`: el índice para buscar (`inicio.md`).

## Cómo está conectado

Cada concepto tiene su nota en `conceptos/`, y cada lección termina con sus enlaces de navegación. Los enlaces son Markdown normal: funcionan en GitHub, en Obsidian y en cualquier editor.

## Consultar con IA (opcional)

No hace falta para usar los apuntes. Si quieres consultarlos con un asistente de IA, hay guías en:

- [consultar-con-gemini.md](consultar-con-gemini.md): con Gemini, usando `cerebro/inicio.md`.
- [tutorial-ollama.md](tutorial-ollama.md): con un modelo local, sin conexión.
- [obsidian-plugins.md](obsidian-plugins.md): plugins de Obsidian que se usaron para esto.

## Ejemplos y datos

Los ejemplos de código y de bases de datos son de práctica. Algunos contienen datos ficticios que pueden parecerse a datos reales. No los uses tal cual en un entorno de producción.

## Mantener

Lee [MANTENIMIENTO.md](MANTENIMIENTO.md). Después de editar, ejecuta `python3 herramientas/mantenimiento.py actualizar`.

## Licencia

MIT. Ver [LICENSE](LICENSE).
