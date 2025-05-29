#!/bin/bash
echo "----------------------------------"
echo "[SETUP] Verificando entorno virtual..."

if [ ! -d "venv" ]; then
  echo "[SETUP] Entorno virtual no encontrado. Creando..."
  python3 -m venv venv
fi

echo "----------------------------------"
echo "[SETUP] Activando entorno virtual..."
source venv/bin/activate

echo "----------------------------------"
echo "[SETUP] Instalando dependencias..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

echo "----------------------------------"
echo "[SETUP] Setup completo. Listo para ejecutar la app."
