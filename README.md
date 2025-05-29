# 🧠 TodoList + MCP API — FastAPI Implementation

Este proyecto es una implementación de una API REST para gestionar listas de tareas (*TodoLists*) y sus ítems, extendida con la intención de ser integrada a un servidor **MCP (Model Context Protocol)**.

Desarrollado como parte de una prueba técnica para la posición de **Jr AI Full Stack Developer** en Crunchloop.

---

## 🚀 Features

✅ Gestión de listas de tareas
✅ CRUD básico de ítems y listas dentro de una lista
✅ Backend RESTful con FastAPI
✅ Frontend moderno con React + Vite 
✅ Documentación automática vía Swagger
✅ Scripts de ejecución multiplataforma (Windows, MacOS, Linux)

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
- Node.js / npm
- React + Vite

---

## 🛠️ Instalación y ejecución

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

## 📌 Endpoints principales
- `POST /lists`: Crear una lista
- `GET /lists`: Obtener todas las listas
- `POST /items/{list_id}`: Crear un ítem en una lista
- `PUT /items/{item_id}`: Actualizar un ítem
- `PATCH /items/{item_id}/complete`: Marcar ítem como completo
- `DELETE /items/{item_id}`: Eliminar un ítem