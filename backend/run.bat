@echo off
echo ----------------------------------
echo [RUN] Verificando entorno virtual...

if not exist "venv\" (
    echo [RUN] Entorno virtual no encontrado. Ejecutando setup...
    call setup.bat
)

echo ----------------------------------
echo [RUN] Activando entorno virtual...
call venv\Scripts\activate

echo ----------------------------------
echo [RUN] Iniciando servidor FastAPI...
start http://127.0.0.1:8000/docs
uvicorn app.main:app --reload

pause