#!/bin/bash

echo "Iniciando BACKEND..."
(cd backend && ./run.sh) &

echo "Iniciando FRONTEND..."
(cd frontend && ./run.sh) &

echo "Ambos servidores fueron lanzados en segundo plano."
wait
echo "Todos los procesos han finalizado."