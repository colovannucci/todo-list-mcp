from sqlalchemy.orm import Session
from app import crud, schemas


def create_list(db: Session, list_data: schemas.TodoListCreate):
    return crud.lists.create_list(db, list_data)


def get_list(db: Session, list_id: int):
    return crud.lists.get_list(db, list_id)


def update_list(db: Session, list_id: int, list_data: schemas.TodoListUpdate):
    return crud.lists.update_list(db, list_id, list_data)


def delete_list(db: Session, list_id: int):
    return crud.lists.delete_list(db, list_id)


def get_all_lists(db: Session):
    return crud.lists.get_all_lists(db)


def get_by_name(db: Session, name: str):
    return crud.lists.get_list_by_name(db, name)
