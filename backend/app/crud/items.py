from sqlalchemy.orm import Session
from .. import models, schemas

def create_item(db: Session, list_id: int, item_data: schemas.TodoItemCreate):
    db_item = models.TodoItem(**item_data.dict(), list_id=list_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item(db: Session, item_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.id == item_id).first()

def update_item(db: Session, item_id: int, item_data: schemas.TodoItemUpdate):
    db_item = get_item(db, item_id)
    if db_item:
        for attr, value in item_data.dict(exclude_unset=True).items():
            setattr(db_item, attr, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def complete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db_item.completed = True
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, item_id: int):
    db_item = get_item(db, item_id)
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

def get_items_for_list(db: Session, list_id: int):
    return db.query(models.TodoItem).filter(models.TodoItem.list_id == list_id).all()

def uncomplete_item(db: Session, item_id: int):
    item = get_item(db, item_id)
    if item:
        item.completed = False
        db.commit()
        db.refresh(item)
    return item
