---
titulo: "Apuntes de aprendizaje autodidacta"
tags: ["portada"]
---

# Apuntes de aprendizaje autodidacta

Apuntes de estudio sobre bases de datos (SQL, MySQL y PostgreSQL), JavaScript con Node.js, Express e inteligencia artificial. Están ordenados para estudiarlos en secuencia y para encontrar un tema en segundos.

No es un curso oficial. Es un registro vivo que se corrige y se amplía con el tiempo.

## Cómo buscar un tema

1. Abre [cerebro/inicio.md](cerebro/inicio.md). Tiene todos los conceptos agrupados por categoría, cada uno con una definición breve.
2. Si buscas una sección concreta de una lección, abre [cerebro/lecciones.md](cerebro/lecciones.md).
3. Pulsa `Ctrl+F` y escribe el tema, en español o en inglés (por ejemplo `trigger`, `foreign key`, `SOLID` o `middleware`).

## Lecciones

Cada área es una carpeta con sus lecciones numeradas. Estudia las áreas en este orden.

<!-- auto:areas -->
1. [Bases de datos](bases-de-datos/indice.md): 5 lecciones
2. [MySQL](mysql/indice.md): 10 lecciones
3. [PostgreSQL](postgresql/indice.md): 7 lecciones
4. [Node.js](nodejs/indice.md): 8 lecciones
5. [Inteligencia artificial](inteligencia-artificial/indice.md): 9 lecciones
6. [Express](express/indice.md): 4 lecciones
<!-- /auto:areas -->

## Conceptos

Los conceptos están agrupados por categoría. Un concepto general, como [dato](conceptos/fundamentos/dato.md), [base de datos](conceptos/bases-de-datos/base-de-datos.md) o [DTO](conceptos/ingenieria/dto.md), sirve para cualquier tecnología. Las tecnologías concretas, como [MySQL](conceptos/motores/mysql.md) o [Express](conceptos/web/express.md), tienen su propia categoría y se apoyan en los conceptos generales.

<!-- auto:categorias -->
1. [Fundamentos](conceptos/fundamentos/categoria.md): 3 conceptos
2. [Bases de datos](conceptos/bases-de-datos/categoria.md): 18 conceptos
3. [SQL](conceptos/sql/categoria.md): 8 conceptos
4. [Motores de base de datos](conceptos/motores/categoria.md): 2 conceptos
5. [Acceso a datos desde una aplicación](conceptos/acceso-a-datos/categoria.md): 4 conceptos
6. [Programación orientada a objetos](conceptos/programacion/categoria.md): 3 conceptos
7. [Ingeniería de software](conceptos/ingenieria/categoria.md): 8 conceptos
8. [Node.js y herramientas](conceptos/nodejs/categoria.md): 5 conceptos
9. [Web y APIs](conceptos/web/categoria.md): 12 conceptos
10. [Formatos de datos](conceptos/formatos/categoria.md): 2 conceptos
11. [Inteligencia artificial](conceptos/inteligencia-artificial/categoria.md): 9 conceptos
<!-- /auto:categorias -->

## Cerebro

La carpeta `cerebro/` contiene los índices para buscar y para consultar con IA:

* `inicio.md`: los conceptos por categoría, con su definición.
* `lecciones.md`: cada lección con sus secciones.

## Cómo está organizado

* Cada lección es un archivo `NN-nombre.md` dentro de la carpeta de su área.
* Cada concepto es un archivo dentro de una carpeta de `conceptos/`. Cada carpeta tiene un `categoria.md` que describe su tema.
* Los enlaces son Markdown normal: funcionan en GitHub, en Obsidian y en cualquier editor.

## Consultar con IA (opcional)

No hace falta para usar los apuntes. Si quieres consultarlos con un asistente de IA, hay guías en:

* [consultar-con-gemini.md](consultar-con-gemini.md): con Gemini, usando los archivos de `cerebro/`.
* [tutorial-ollama.md](tutorial-ollama.md): con un modelo local, sin conexión.
* [obsidian-plugins.md](obsidian-plugins.md): plugins de Obsidian que se usaron para esto.

## Ejemplos y datos

Los ejemplos de código y de bases de datos son de práctica. Algunos contienen datos ficticios que pueden parecerse a datos reales. No los uses tal cual en un entorno de producción.

## Mantener

Lee [MANTENIMIENTO.md](MANTENIMIENTO.md). Después de editar, ejecuta `python3 herramientas/mantenimiento.py actualizar`.

## Licencia

MIT. Ver [LICENSE](LICENSE).
