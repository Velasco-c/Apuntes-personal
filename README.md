---
titulo: "Apuntes de aprendizaje autodidacta"
tags: ["portada"]
---

# Apuntes de aprendizaje autodidacta

Colección de apuntes de información autodidacta sobre bases de datos, programación e inteligencia artificial. Está ordenada para estudiarla en secuencia y para consultarla cuando hace falta.

No es un curso oficial. Es un registro vivo que se corrige y se amplía con el tiempo.

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

Los temas se enlazan a través de `conceptos/`, una nota por concepto. Cada concepto muestra en qué lecciones aparece y qué conceptos le acompañan. Cada lección termina con su navegación y sus conceptos.

Abre la carpeta como bóveda de Obsidian para ver el grafo. Los enlaces son Markdown estándar, así que también funcionan en GitHub.

## Asistente local con IA

[Tutorial de Ollama](tutorial-ollama.md): instala un modelo pequeño (`qwen2.5:1.5b`) y conéctalo con Obsidian. Para preguntas generales, usa como nota actual [cerebro/glosario.md](cerebro/glosario.md) o el mapa de un área: son resúmenes compactos que gastan pocos tokens.

## Mantener y ampliar

Lee [MANTENIMIENTO.md](MANTENIMIENTO.md). Después de cualquier cambio, ejecuta `python3 herramientas/mantenimiento.py actualizar`.

## Licencia

MIT. Ver [LICENSE](LICENSE).
