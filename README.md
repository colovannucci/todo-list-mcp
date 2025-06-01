# 📝 TodoList MCP App

Aplicación full stack con backend FastAPI y frontend React que implementa una API de gestión de tareas y listas, junto a un servidor compatible con [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol).

## 🚀 Funcionalidades

- Gestión de listas y tareas con FastAPI + SQLLite.
- Cliente React+Vite junto con manipulador de listas y tareas.
- COnfiguración generada para realizar interacción natural con aplicación Claude Desktop.
---

## 📸 Demo

> El backend estará disponible en: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

> El frontend estará disponible en: [http://localhost:5173/](http://localhost:5173/)

---

## 🧱 Stack Tecnológico

**Backend**
- Python 3.11+
- FastAPI
- Uvicorn
- SQLite
- SQLAlchemy
- Pydantic

**Frontend:**
- Node.js 16+ y npm
- React + Vite

---

## 💡 Requerimientos previos

Este proyecto requiere tener las siguientes tecnologías instaladas para instalar sus dependencias correctamente.

- Python [Descarga Python](https://www.python.org/downloads/)
- Node + npm. [Descarga Node](https://nodejs.org/es/)
- Claude desktop. [Descarga Claude](https://claude.ai/download)

## 🛠️ Instalación y ejecución

El Backend y Frontend cuentan con scripts que instalarán todas las dependencias automáticamente para que no deba preocuparse por ningún aspecto.
Deberá realizar una mínima configuración en la aplicación Claude Desktop.

### 🔵 En Windows

```bat
./run_dev.bat
```

### 🔵 En MAC/Linux/WSL

```bash
chmod +x run_dev.sh
chmod +x backend/run.sh
chmod +x frontend/run.sh
./run_dev.sh
```

### 🔵 Claude Desktop

- Habilitar conexión servidor MCP.

1- Abrir aplicación
2- Selecciona en la esquina superior izquierda la opción "Archivo" -> "Configuración".
3- Dirigirse a pestaña "Desarrollador".
4- Presionar botón "Editar configuración".
5- Seleccionar y abirir archivo "claude_desktop_config".
6- Reemplazar el contenido por el archivo clonado en este repositorio.
7- Reiniciar aplicación. 

- Ejemplos de conversación.

Deberá seleccionar manualmente "permitir X herramienta externa".

```
Que listas tengo en este momento?
Quisiera ver los items de la lista X.
Crea la lista X.
```
