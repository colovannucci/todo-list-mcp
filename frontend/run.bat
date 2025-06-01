@echo off
echo ----------------------------------
echo [RUN] Verificando directorio de la aplicacion...
cd app
REM Verifica si las dependencias están instaladas
if not exist node_modules (
    echo Instalando dependencias...
    npm install
) else (
    echo Dependencias ya instaladas.
)

REM Inicia el servidor de desarrollo y abre el navegador
echo Iniciando servidor de desarrollo de Vite...
start http://localhost:5173
call npx vite
pause
