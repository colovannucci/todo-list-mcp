@echo off
echo Iniciando BACKEND...
start cmd /k "cd backend && call run.bat"

echo Iniciando FRONTEND...
start cmd /k "cd frontend && call run.bat"

echo Ambos servidores fueron lanzados en terminales separadas.
pause
