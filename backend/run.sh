#!/bin/bash
echo "----------------------------------"
echo "[RUN] Verificando entorno virtual..."

if [ ! -d "venv" ]; then
  echo "[RUN] Entorno virtual no encontrado. Ejecutando setup..."
  bash setup.sh
fi

echo "----------------------------------"
echo "[RUN] Activando entorno virtual..."
source venv/bin/activate

echo "----------------------------------"
echo "[RUN] Iniciando servidor FastAPI..."
open http://127.0.0.1:8000/docs
uvicorn app.main:app --reload