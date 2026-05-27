import os
import yt_dlp

def obtener_ruta_descargas():
    carpeta = os.path.join(os.path.expanduser("~"), "Downloads", "descargas")
    os.makedirs(carpeta, exist_ok=True)
    return carpeta

def descargar(url, formato):
    carpeta_destino = obtener_ruta_descargas()

    if formato == "audio":
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
            'noplaylist': True,
        }
    else:  # video
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(carpeta_destino, '%(title)s.%(ext)s'),
            'noplaylist': True,
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("✅ Descarga completada.")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    url = input("URL del video: ")
    formato = input("Formato (video/audio): ").strip().lower()

    if formato not in ["video", "audio"]:
        formato = "video"

    descargar(url, formato)