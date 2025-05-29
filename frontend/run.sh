#!/bin/bash
cd app || exit

# Verifica si las dependencias están instaladas
if [ ! -d "node_modules" ]; then
    echo "Instalando dependencias..."
    npm install
else
    echo "Dependencias ya instaladas."
fi

# Inicia el servidor de desarrollo y abre el navegador
echo "Iniciando servidor de desarrollo de Vite..."
xdg-open http://localhost:5173 >/dev/null 2>&1 || open http://localhost:5173 >/dev/null 2>&1
npx vite
