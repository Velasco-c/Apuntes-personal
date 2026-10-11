---
titulo: "Plugins de Obsidian recomendados"
tags: ["tutorial", "obsidian"]
---

# Plugins de Obsidian recomendados

Plugins que usamos en este repositorio, con la configuración recomendada y alternativas. Son de la comunidad y se buscan en *Configuración → Complementos comunitarios → Explorar*.

Antes de activar cualquier plugin, revisa su página de GitHub, los permisos que pide y la fecha de su última actualización. Varias fichas de la tienda dicen que el plugin "no ha sido revisado manualmente por el equipo de Obsidian".

## Resumen

| Plugin | Para qué | Dónde corre | Uso |
| --- | --- | --- | --- |
| Gemini Scribe | Consultar los apuntes con Gemini | Nube (Google) | Recomendado |
| Ollama Notes Chat | Chatear con un modelo local | Tu equipo (Ollama) | Recomendado, sin conexión |
| Smart Environment + Smart Connections | Ver notas relacionadas | Tu equipo | Opcional |

## Gemini: Gemini Scribe

Autor: Allen Hutchison. Guía completa: [consultar-con-gemini.md](consultar-con-gemini.md).

### Opciones recomendadas

| Ajuste | Valor | Por qué |
| --- | --- | --- |
| Proveedores | Gemini | Es la IA de nube que usamos. |
| Clave de API | Tu clave de Google AI Studio | Sin ella no funciona. |
| Modelo | Gemini 2.5 Flash | Rápido y con nombre fijo. |
| Revisar las diferencias antes de escribir los archivos | Activado | Ningún cambio se aplica sin que lo veas. |
| Conservar el historial de sesiones | Desactivado | Evita que las conversaciones se guarden como archivos en la bóveda. |
| Índice de búsqueda de la bóveda | Desactivado | Evita enviar tus notas a Google para indexarlas. |
| Funciones | Sin investigación web | Así las respuestas salen de tus apuntes. Si la opción existe, desactívala. |
| Hooks de ciclo de vida | Desactivado | No ejecuta acciones automáticas. |
| Carpeta del plugin | `gemini-scribe` (la de por defecto) | Agrégala al `.gitignore`. |

### Alternativas de Gemini

- **Gemini Helper** (TAKESHI MORITA): chat, flujos de trabajo y búsqueda semántica. Tiene más funciones, pero no ha sido revisado manualmente por Obsidian. Úsalo solo si necesitas buscar por significado.
- **Gemini AI Assistant** y **Gemini Assistant**: no se han actualizado en años. No los recomendamos.

## Ollama: Ollama Notes Chat

Para consultar sin conexión. Requiere Ollama instalado en tu equipo. Guía completa: [tutorial-ollama.md](tutorial-ollama.md).

### Opciones recomendadas

| Ajuste | Valor | Por qué |
| --- | --- | --- |
| Base URL | `http://localhost:11434` | Ollama corre en tu equipo. |
| Allow data to leave this computer | Desactivado | Tus notas no salen de tu equipo. |
| Model | `qwen2.5:1.5b` | El único modelo que necesitamos. |
| Temperature | 0.3 | Respuestas más fieles a tus apuntes. El valor por defecto (0.7) inventa más. |
| Max tokens per response | 1024 | Deja espacio para el contexto dentro de los 4096 tokens que Ollama usa en tu equipo. |
| Default model context limit | 4096 | Coincide con el límite real de Ollama. Por defecto aparece 8192, que no se alcanza en tu equipo. |
| System prompt | El de abajo | Obliga a responder con tus notas. |

System prompt recomendado:

> Responde en español usando solo el contexto que te doy. Si el contexto no responde la pregunta, dilo. Cita la sección de donde sacas cada dato.

### Alternativas de Ollama

- **Smart Connections**: no chatea, pero muestra notas relacionadas. Usa un modelo que corre dentro de Obsidian, así que no depende de Ollama.
- Existen otros plugins para chatear con Ollama. No los recomendamos aquí porque no los hemos probado.

## Smart Environment y Smart Connections (opcional)

- Instala primero **Smart Environment**, porque Smart Connections lo necesita.
- En Smart Environment, en **Default embedding model**, elige *Multilingual E5 Small* (Transformers). Se ejecuta en tu equipo.
- Después de cambiar el modelo, pulsa **Reset data** para regenerar los datos.

## Plugins que no recomendamos

- **Nexus, OmniChat, VaultAI** y las versiones de Gemini Helper para varios proveedores: mezclan varias IA, así que tus notas pueden ir a más de un servicio. Para este repositorio no hacen falta.
- **LLM Hub, EngramQuest y UltraSearch**: no tienen relación con los apuntes de este repositorio.
- Cualquier plugin que pida una clave o una cuenta sin que sepas qué hace con tus notas.

## Privacidad

- Con Gemini, el texto que envías sale de tu equipo hacia Google. Revisa sus condiciones antes de consultar notas privadas.
- Con Ollama y Smart Connections, todo se queda en tu equipo.

## Datos locales

Algunos plugins guardan datos en la raíz de tu bóveda. Esas carpetas no deben subirse a GitHub. La lista está en la sección de `.gitignore` del [README](README.md).