from .database import SessionLocal
from sqlalchemy.orm import Session
from typing import Generator

# Dependencia para inyectar una sesión de base de datos en los endpoints.
# Utiliza un generador para garantizar que la sesión se cierre correctamente,
# incluso si ocurre una excepción durante el request.
def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db  # Proporciona la sesión activa al endpoint
    finally:
        db.close()  # Cierra la sesión al finalizar el request (éxito o error)
