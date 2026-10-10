---
titulo: "Apuntes de aprendizaje autodidacta"
tags: ["portada"]
---

# Apuntes de aprendizaje autodidacta

Este repositorio es una **colección de apuntes de información autodidacta**: lo que voy aprendiendo por mi cuenta sobre bases de datos, programación con JavaScript e inteligencia artificial, organizado para consultarlo cuando lo necesito y para que cada tema esté conectado con los demás.

No es un curso oficial ni un libro terminado. Es un registro vivo: se corrige, se amplía y se reorganiza conforme avanzo.

## Por dónde empezar

Los temas siguen un orden de estudio. Cada área tiene su índice, y el [mapa de contenidos](MAPA.md) reúne todo en una sola página.

1. [Bases de datos](bases-de-datos/indice.md): modelo relacional, diseño conceptual, normalización y modelado. Es la base del resto.
2. [MySQL](mysql/indice.md): SQL desde cero, hasta procedimientos, vistas, triggers y eventos.
3. [PostgreSQL](postgresql/indice.md): consultas avanzadas, funciones de ventana, datos JSON y XML.
4. [Node.js](nodejs/indice.md): programación orientada a objetos, principios de diseño y persistencia con MySQL.
5. [Inteligencia artificial](inteligencia-artificial/indice.md): redes neuronales, prompts, alucinaciones, MCP y testing automatizado con IA.

## Cómo está conectado

Los apuntes se enlazan a través de la carpeta `conceptos/`. Cada concepto, por ejemplo [Transacción](conceptos/transaccion.md) o [Trigger](conceptos/trigger.md), es una nota propia que aparece en varias lecciones y que muestra en cuáles se usa. Cada lección termina con enlaces de navegación y la lista de conceptos que contiene.

Los ejercicios y prácticas están dentro de cada lección, junto a la teoría.

## Cómo usarlo en Obsidian

Abre la carpeta como una bóveda de Obsidian. Los enlaces están escritos en Markdown estándar, así que funcionan en Obsidian, en GitHub y en cualquier editor. El grafo de Obsidian muestra la red de temas. El archivo `grafo.json` describe la misma red en un formato que pueden leer programas y modelos de IA.

## Estructura

- `bases-de-datos/`, `mysql/`, `postgresql/`, `nodejs/` e `inteligencia-artificial/`: lecciones por área.
- `conceptos/`: notas de concepto compartidas por todas las áreas.
- `herramientas/`: script para regenerar los índices y validar los enlaces.
- [MAPA.md](MAPA.md): índice maestro. [MANTENIMIENTO.md](MANTENIMIENTO.md): convenciones del repositorio.

## Licencia

MIT. Ver [LICENSE](LICENSE).
