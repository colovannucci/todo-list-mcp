from sqlalchemy.orm import Session
from app import crud, schemas


def create_item(db: Session, list_id: int, item_data: schemas.TodoItemCreate):
    return crud.items.create_item(db, list_id, item_data)


def update_item(db: Session, item_id: int, item_data: schemas.TodoItemUpdate):
    return crud.items.update_item(db, item_id, item_data)


def complete_item(db: Session, list_id: int, item_title: str) -> str:
    items = crud.items.get_items_for_list(db, list_id)
    match = next((i for i in items if i.title.lower() == item_title.lower()), None)

    if not match:
        return f"No se encontró tarea '{item_title}' en la lista"

    crud.items.complete_item(db, match.id)
    return f"Ítem '{match.title}' marcado como completado"


def uncomplete_item(db: Session, list_id: int, item_title: str) -> str:
    items = crud.items.get_items_for_list(db, list_id)
    match = next((i for i in items if i.title.lower() == item_title.lower()), None)

    if not match:
        return f"No se encontró tarea '{item_title}' en la lista"

    crud.items.uncomplete_item(db, match.id)
    return f"Ítem '{match.title}' marcado como no completado"


def delete_item(db: Session, list_id: int, item_title: str) -> str:
    items = crud.items.get_items_for_list(db, list_id)
    match = next((i for i in items if i.title.lower() == item_title.lower()), None)

    if not match:
        return f"No se encontró tarea '{item_title}' en la lista"

    crud.items.delete_item(db, match.id)
    return f"Ítem '{match.title}' eliminado correctamente"


def list_items(db: Session, list_id: int):
    return crud.items.get_items_for_list(db, list_id)


def get_item(db: Session, item_id: int):
    return crud.items.get_item(db, item_id)
