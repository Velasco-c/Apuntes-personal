---
titulo: "Tutorial: asistente local con Ollama y qwen2.5:1.5b"
tags: ["tutorial", "ia"]
---

# Tutorial: asistente local con Ollama y qwen2.5:1.5b

Instala un modelo pequeño que corre en tu equipo y conéctalo con Obsidian. Usa un solo modelo: `qwen2.5:1.5b`. Después de la descarga no necesita internet.

Requisitos: 8 GB de RAM y 2 GB de disco. No necesitas tarjeta gráfica.

## 1. Instalar Ollama

- **Arch o CachyOS:** `sudo pacman -S ollama`
- **Ubuntu, Debian, Fedora u otra distribución:** `curl -fsSL https://ollama.com/install.sh | sh`
- **macOS o Windows:** instalador en [ollama.com/download](https://ollama.com/download)

No instales `ollama-cuda` salvo que tu GPU lo soporte. Ver problemas frecuentes.

## 2. Arrancar y comprobar

En Linux:

```bash
sudo systemctl enable --now ollama
systemctl is-active ollama
```

Debe responder `active`. En todos los sistemas, este comando debe devolver la versión en JSON:

```bash
curl http://127.0.0.1:11434/api/version
```

## 3. Descargar el modelo

```bash
ollama pull qwen2.5:1.5b
ollama run qwen2.5:1.5b "Di hola en una frase"
```

## 4. Chat en Obsidian: Ollama Notes Chat

Instala **Ollama Notes Chat** desde *Complementos comunitarios* y ajusta:

- **Base URL:** `http://localhost:11434`. Pulsa **Test**.
- **Allow data to leave this computer:** apagado. Así el contenido de tus notas no sale del equipo.
- **Model:** `qwen2.5:1.5b`.

## 5. Conexiones en Obsidian: Smart Connections (sin Ollama)

Smart Connections calcula las similitudes con un modelo que corre dentro de Obsidian:

1. Abre *Ajustes → Smart Environment*.
2. En **Default embedding model**, elige **Multilingual E5 Small**. Si no aparece, pulsa **+ New**, elige **Transformers** y en *Model* selecciona **Multilingual E5 Small**.
3. Baja a **Reset data** y pulsa **Reset data**. La primera indexación tarda unos minutos.

## 6. Usar el chat con pocos tokens

En el menú **Context** de la vista de chat:

- **Current note:** para preguntar sobre un concepto.
- **Current selection:** para preguntar sobre una sección de una lección larga. Selecciónala antes de preguntar.
- **No context:** para preguntas generales.

Para preguntas sobre todo el repositorio, usa `cerebro/glosario.md` como nota actual, o el mapa de un área (`cerebro/mapa-mysql.md`, por ejemplo) para saber dónde está un tema.

## Problemas frecuentes

- **El servicio se reinicia sin parar.** Revisa `journalctl -u ollama -n 50 --no-pager`. Si aparece `panic: bad origin`, borra la variable `OLLAMA_ORIGINS` de la configuración del servicio. No la necesitas para Obsidian:

```bash
sudo rm -rf /etc/systemd/system/ollama.service.d
sudo systemctl daemon-reload
sudo systemctl restart ollama
```

- **`skipping CUDA device — compute capability not in compiled architectures`.** Tu GPU es demasiado antigua para ese paquete. Por ejemplo, la GTX 1050 tiene compute capability 6.1. Usa la versión de CPU, que funciona bien con modelos pequeños. Para comprobar tu GPU: `nvidia-smi --query-gpu=name,compute_cap --format=csv`.
- **Las respuestas parecen cortadas.** En la prueba de este tutorial, Ollama usó 4096 tokens de contexto. Reduce el texto enviado con *Current selection* o con un archivo de `cerebro/`.
- **`ollama pull` falla por conexión.** Espera unos segundos a que el servicio arranque y repite el comando.
