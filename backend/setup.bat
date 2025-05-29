@echo off
echo ----------------------------------
echo [SETUP] Creando entorno virtual...
py -m venv venv

echo ----------------------------------
echo [SETUP] Activando entorno virtual...
call venv\Scripts\activate

echo ----------------------------------
echo [SETUP] Instalando dependencias...
py -m pip install --upgrade pip
py -m pip install -r requirements.txt

echo ----------------------------------
echo [SETUP] Setup completo. Listo para ejecutar la app.