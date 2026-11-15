import os
import sys
import uuid
import threading
import webbrowser
from flask import Flask, render_template, request, jsonify
import yt_dlp

if getattr(sys, 'frozen', False):
    template_dir = os.path.join(sys._MEIPASS, 'templates')
    app = Flask(__name__, template_folder=template_dir)
else:
    app = Flask(__name__)

tasks = {}

def obtener_ruta_descargas():
    carpeta = os.path.join(os.path.expanduser("~"), "Downloads", "descargas")
    os.makedirs(carpeta, exist_ok=True)
    return carpeta

def ejecutar_descarga(task_id, url, formato):
    carpeta_destino = obtener_ruta_descargas()

    def progress_hook(d):
        if d['status'] == 'downloading':
            total = d.get('total_bytes') or d.get('total_bytes_estimate') or 0
            descargado = d.get('downloaded_bytes', 0)
            porcentaje = round((descargado / total) * 100, 1) if total > 0 else 0
            tasks[task_id].update({
                'status': 'downloading',
                'percent': porcentaje,
                'speed': d.get('_speed_str', '').strip(),
                'eta': d.get('_eta_str', '').strip()
            })
        elif d['status'] == 'finished':
            tasks[task_id].update({
                'status': 'processing',
                'percent': 100
            })

    plantilla_salida = os.path.join(carpeta_destino, '%(extractor)s - %(title).80s.%(ext)s')

    ydl_opts = {
        'outtmpl': plantilla_salida,
        'noplaylist': True,
        'no_color': True,
        'progress_hooks': [progress_hook],
        'quiet': True,
    }

    if formato == "audio":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '320',
            }],
        })
    elif formato == "720p":
        ydl_opts.update({
            'format': 'bestvideo[height<=720][ext=mp4]+bestaudio[ext=m4a]/best[height<=720][ext=mp4]/best[height<=720]',
            'merge_output_format': 'mp4',
        })
    else:
        ydl_opts.update({
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'merge_output_format': 'mp4',
        })

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get('title', 'Archivo descargado')
        tasks[task_id].update({
            'status': 'completed',
            'percent': 100,
            'title': titulo,
            'folder': carpeta_destino
        })
    except Exception as e:
        tasks[task_id].update({
            'status': 'error',
            'error': str(e)
        })

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/info', methods=['POST'])
def obtener_info():
    url = request.json.get('url', '').strip()
    if not url:
        return jsonify({'error': 'URL vacía'}), 400
    try:
        ydl_opts = {'quiet': True, 'noplaylist': True, 'no_color': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return jsonify({
                'title': info.get('title', 'Sin título'),
                'thumbnail': info.get('thumbnail', ''),
                'platform': info.get('extractor_key', 'Web'),
                'duration': info.get('duration_string', '')
            })
    except Exception as e:
        return jsonify({'error': f'No se pudo leer el enlace: {str(e)}'}), 400

@app.route('/api/download', methods=['POST'])
def iniciar_descarga():
    data = request.json
    url = data.get('url', '').strip()
    formato = data.get('formato', 'video')

    if not url:
        return jsonify({'error': 'Debés ingresar una URL'}), 400

    task_id = str(uuid.uuid4())
    tasks[task_id] = {'status': 'starting', 'percent': 0}

    hilo = threading.Thread(target=ejecutar_descarga, args=(task_id, url, formato))
    hilo.start()

    return jsonify({'task_id': task_id})

@app.route('/api/status/<task_id>')
def estado_descarga(task_id):
    task = tasks.get(task_id)
    if not task:
        return jsonify({'error': 'Tarea no encontrada'}), 404
    return jsonify(task)

if __name__ == '__main__':
    print("🚀 Servidor iniciado en http://127.0.0.1:5000")
    threading.Timer(1.2, lambda: webbrowser.open("http://127.0.0.1:5000")).start()
    app.run(debug=False, port=5000)
