---
titulo: "Apuntes de aprendizaje autodidacta"
tags: ["portada"]
---

# Apuntes de aprendizaje autodidacta

Colección de apuntes de información autodidacta sobre bases de datos, programación e inteligencia artificial. Está ordenada para estudiarla en secuencia y para consultarla cuando hace falta.

No es un curso oficial. Es un registro vivo que se corrige y se amplía con el tiempo.

## Acceso rápido

| Quiero... | Ir a | Resultado |
| --- | --- | --- |
| Empezar a estudiar | [Bases de datos](bases-de-datos/indice.md) | Ruta de estudio en orden. |
| Buscar un concepto | [Inicio: mapa rápido](cerebro/inicio.md) | Conceptos agrupados por categoría, con su definición. |
| Buscar una sección de una lección | [Lecciones por secciones](cerebro/lecciones.md) | Cada lección con sus secciones. |
| Consultar con Gemini | [Tutorial de Gemini](consultar-con-gemini.md) | Cómo usar un solo archivo con Gemini. |
| Consultar sin conexión | [Tutorial de Ollama](tutorial-ollama.md) | Modelo local, como último recurso. |
| Ver el mapa completo | [Mapa de contenidos](MAPA.md) | Todas las lecciones y conceptos. |
| Añadir o mantener contenido | [Guía de mantenimiento](MANTENIMIENTO.md) | Comandos y convenciones. |

## Por dónde empezar

Estudia las áreas en este orden. Cada una tiene su índice con las lecciones.

<!-- auto:areas -->
1. [Bases de datos](bases-de-datos/indice.md): 5 lecciones
2. [MySQL](mysql/indice.md): 10 lecciones
3. [PostgreSQL](postgresql/indice.md): 7 lecciones
4. [Node.js](nodejs/indice.md): 8 lecciones
5. [Inteligencia artificial](inteligencia-artificial/indice.md): 9 lecciones
<!-- /auto:areas -->

## Cómo está conectado

Los conceptos están en `conceptos/`, una nota por concepto, agrupados en carpetas por categoría. Cada carpeta tiene un `categoria.md` que describe su tema. Cada lección termina con su navegación entre lecciones.

Abre la carpeta como bóveda de Obsidian para ver el grafo. Los enlaces son Markdown estándar, así que también funcionan en GitHub.

## Consultar con IA

Hay dos tutoriales, según tengas o no conexión. [Gemini](consultar-con-gemini.md) es la opción principal. [Ollama](tutorial-ollama.md) queda como último recurso sin conexión. Los dos usan los archivos de `cerebro/`: [inicio.md](cerebro/inicio.md), con los conceptos por categoría, y [lecciones.md](cerebro/lecciones.md), con las secciones de cada lección. Los plugins de Obsidian que usamos, con su configuración, están en [obsidian-plugins.md](obsidian-plugins.md).

## Mantener y ampliar

Lee [MANTENIMIENTO.md](MANTENIMIENTO.md). Después de cualquier cambio, ejecuta `python3 herramientas/mantenimiento.py actualizar`.

## Opciones de `.gitignore` para tu bóveda

La carpeta `.obsidian/` ya está ignorada: guarda tu configuración personal. Algunos plugins, en cambio, crean carpetas de datos en la raíz de la bóveda, y esas sí conviene ignorarlas para no subirlas a GitHub. Agrega a tu `.gitignore` solo las que uses:

- **Gemini Scribe** (ver [obsidian-plugins.md](obsidian-plugins.md)):

```
  gemini-scribe/
  Agent-Sessions/
```

  `Agent-Sessions/` solo aparece si activas el historial de sesiones.

- **Otros plugins:** si un plugin crea una carpeta nueva en la raíz, búscala en el explorador de archivos y agrégala con el mismo formato.

## Licencia

MIT. Ver [LICENSE](LICENSE).