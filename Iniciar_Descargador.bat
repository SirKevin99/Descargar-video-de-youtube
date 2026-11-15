@echo off
title Descargador Multimedia (YT - TikTok - IG - FB)
cd /d "%~dp0"

if not exist "venv\Scripts\python.exe" (
    echo Configurando entorno por primera vez...
    python -m venv venv
    call venv\Scripts\activate.bat
    pip install -r requirements.txt
) else (
    call venv\Scripts\activate.bat
)

echo Iniciando aplicacion en http://127.0.0.1:5000 ...
python app.py
pause
