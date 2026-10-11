---
titulo: "Consultar mis apuntes con Gemini"
tags: ["tutorial", "ia"]
---

# Consultar mis apuntes con Gemini

Gemini puede responder con tus apuntes si le das un solo archivo: `cerebro/inicio.md`. Ese archivo tiene las tablas de conceptos y lecciones, con enlaces a cada sección. No necesitas plugins ni instalar nada.

## Qué necesitas

- Una cuenta de Google.
- El archivo `cerebro/inicio.md`. Si cambiaste tus apuntes, ejecuta antes `python3 herramientas/mantenimiento.py actualizar` para regenerarlo.

## Opción 1: un Gem con tus apuntes (recomendada)

Un Gem es un asistente guardado con sus instrucciones y sus archivos. Si tu cuenta no tiene Gems, usa la opción 2.

1. En [gemini.google.com](https://gemini.google.com), abre **Gems** y pulsa **Nuevo Gem**.
2. Ponle el nombre `Apuntes`.
3. En las instrucciones, pega esto:

> Responde solo con la información del archivo que te subí, que es el índice de mis apuntes de estudio. Usa sus tablas para ubicar el concepto y dime la lección y la sección donde se explica. Si el tema no está en el archivo, dilo. Responde en español y sé breve.

4. En los archivos de conocimiento, sube `cerebro/inicio.md`. Si Gemini no acepta la extensión `.md`, copia el archivo y cámbiale el nombre a `inicio.txt`.
5. Guarda el Gem y ábrelo para preguntar.

Para respuestas con más detalle, sube también la lección que te interese, por ejemplo `mysql/09-optimizacion-transacciones-y-particionamiento.md`.

## Opción 2: un chat normal

Abre un chat nuevo, adjunta `cerebro/inicio.md` y escribe la pregunta. Hay que volver a adjuntarlo en cada chat nuevo, porque no se guarda.

## Cómo preguntar

- ¿Qué es ACID y en qué lección se explica?
- ¿Qué diferencia hay entre SOLID y los patrones de diseño?
- Dame un ejemplo rápido de trigger.

Pide siempre la lección y la sección. Así puedes abrirla y comprobar la respuesta.

## Cosas que debes saber

- **Privacidad.** Google procesa lo que subes. En el plan gratuito, Google puede usar tus envíos para mejorar sus productos, según sus condiciones vigentes. Revísalas antes de subir notas privadas.
- **Actualizar.** Cada vez que cambies tus apuntes, vuelve a ejecutar `actualizar` y sube el archivo de nuevo. Si subes una versión vieja, Gemini responderá con datos viejos.
- **Límites.** El plan gratuito tiene límites de uso diario que cambian con el tiempo.

## Problemas frecuentes

- **No acepta el archivo.** Cámbiale la extensión a `.txt`, o pega el contenido en el chat.
- **Responde algo que no está en tus apuntes.** Pide la lección y la sección. Si el tema no aparece en el índice, la respuesta viene del modelo y no de tus notas.
