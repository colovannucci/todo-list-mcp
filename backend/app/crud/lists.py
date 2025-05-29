from sqlalchemy.orm import Session
from .. import models, schemas

def create_list(db: Session, list_data: schemas.TodoListCreate):
    db_list = models.TodoList(name=list_data.name)
    db.add(db_list)
    db.commit()
    db.refresh(db_list)
    return db_list

def get_list(db: Session, list_id: int):
    return db.query(models.TodoList).filter(models.TodoList.id == list_id).first()

def update_list(db: Session, list_id: int, list_data: schemas.TodoListUpdate):
    db_list = get_list(db, list_id)
    if db_list:
        for attr, value in list_data.dict(exclude_unset=True).items():
            setattr(db_list, attr, value)
        db.commit()
        db.refresh(db_list)
    return db_list

def delete_list(db: Session, list_id: int):
    db_list = get_list(db, list_id)
    if db_list:
        db.delete(db_list)
        db.commit()
    return db_list

def get_all_lists(db: Session):
    return db.query(models.TodoList).all()
