# Descargador Multimedia Web (YouTube · TikTok · Instagram · Facebook)

Aplicación web local construida con **Python (Flask)** y **yt-dlp** para descargar videos en MP4 o extraer audio en MP3 (320 kbps) desde múltiples plataformas mediante una interfaz gráfica en el navegador.

## Características

- **Soporte multiplataforma:** Compatible con **YouTube**, **TikTok**, **Instagram** (Reels/Posts) y **Facebook**.
- **Vista previa automática:** Muestra miniatura, título, plataforma y duración antes de descargar.
- **Opciones de formato:**
  - **Video MP4 (Máxima calidad):** Prioriza flujos nativos MP4 para máxima compatibilidad en PC y móviles.
  - **Video 720p:** Versión optimizada y más liviana.
  - **Audio MP3:** Extracción directa a 320 kbps.
- **Progreso en tiempo real:** Barra de descarga en segundo plano con velocidad y tiempo estimado (ETA) sin bloquear la interfaz.

## Requisitos previos

1. **Python 3.10 o superior**
2. **FFmpeg** (necesario para unir pistas de video/audio en MP4 y convertir a MP3):
   - **Windows:** `winget install Gyan.FFmpeg`
   - **Ubuntu/Debian:** `sudo apt install ffmpeg`
   - **Arch Linux:** `sudo pacman -S ffmpeg`

## Instalación y uso

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/SirKevin99/Descargar-video-de-youtube.git
   cd Descargar-video-de-youtube
   ```

2. **Crear y activar un entorno virtual (opcional):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Linux/macOS:
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la aplicación:**
   ```bash
   python app.py
   ```

5. **Abrir en el navegador:**
   Ingresá a `[http://127.0.0.1:5000](http://127.0.0.1:5000)`, pegá el enlace del video y elegí el formato. Los archivos se guardan automáticamente en `~/Downloads/descargas`.

## Versiones

- **`v2.0.0` (Actual):** Migración a interfaz web con Flask, barra de progreso en tiempo real, vista previa y soporte para TikTok, Instagram y Facebook.
- **`v1.0.0`:** Script inicial por línea de comandos (CLI) exclusivo para YouTube.
