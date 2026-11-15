# Descargador Multimedia Web (YouTube · TikTok · Instagram · Facebook)

Aplicación web local construida con **Python (Flask)** y **yt-dlp** para descargar videos en MP4 o extraer audio en MP3 (320 kbps) desde múltiples plataformas mediante una interfaz gráfica en el navegador.

## Características

- **Soporte multiplataforma:** Compatible con **YouTube**, **TikTok**, **Instagram** (Reels/Posts) y **Facebook**.
- **Ejecución con doble clic:** Apertura automática en el navegador mediante `Iniciar_Descargador.bat` o el ejecutable `DescargadorMultimedia.exe`.
- **Vista previa automática:** Muestra miniatura, título, plataforma y duración antes de descargar.
- **Opciones de formato:**
  - **Video MP4 (Máxima calidad):** Prioriza flujos nativos MP4 para máxima compatibilidad en PC y móviles.
  - **Video 720p:** Versión optimizada y más liviana.
  - **Audio MP3:** Extracción directa a 320 kbps.
- **Progreso en tiempo real:** Barra de descarga en segundo plano con velocidad y tiempo estimado (ETA).

## Requisitos previos

- **FFmpeg** (necesario para unir pistas de video/audio en MP4 y convertir a MP3):
  - **Windows:** `winget install Gyan.FFmpeg`
  - **Ubuntu/Debian:** `sudo apt install ffmpeg`
  - **Arch Linux:** `sudo pacman -S ffmpeg`
- **Python 3.10+** (solo si ejecutás desde el código fuente o el `.bat`; no es necesario si usás el `.exe` de la sección *Releases*).

## Uso rápido en Windows

1. **Con ejecutable (sin instalar Python):**
   Descargá `DescargadorMultimedia.exe` desde la sección **Releases** de este repositorio y hacé doble clic. Se abrirá automáticamente `[http://127.0.0.1:5000](http://127.0.0.1:5000)` en tu navegador.
2. **Desde el código fuente (con doble clic):**
   Cloná el repositorio y ejecutá **`Iniciar_Descargador.bat`**. El script crea el entorno virtual, instala dependencias y abre el navegador solo.

## Compilar tu propio `.exe`

```bash
pip install -r requirements.txt pyinstaller
python -m PyInstaller --onefile --add-data "templates;templates" --name "DescargadorMultimedia" app.py
```

El ejecutable generado queda en `dist/DescargadorMultimedia.exe`.

## Versiones

- **`v2.1.0` (Actual):** Apertura automática en navegador, lanzador `Iniciar_Descargador.bat` y soporte para empaquetado `.exe` con PyInstaller.
- **`v2.0.0`:** Interfaz web con Flask, barra de progreso en tiempo real y soporte multiplataforma.
- **`v1.0.0`:** Script inicial por línea de comandos (CLI) exclusivo para YouTube.

- **SirKevin99** — Desarrollo principal.
