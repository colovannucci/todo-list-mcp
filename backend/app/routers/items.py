from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import schemas, crud
from app.dependencies import get_db
from app.utils import http as http_utils

router = APIRouter(prefix="/lists/{list_id}/items", tags=["items"])

@router.post("/", response_model=schemas.TodoItem)
def create_item(list_id: int, item_data: schemas.TodoItemCreate, db: Session = Depends(get_db)):
    # validar que la lista exista
    list_ = crud.lists.get_list(db, list_id)
    http_utils.raise_404_if_none(list_, "List not found")
    return crud.items.create_item(db, list_id, item_data)

@router.get("/{item_id}", response_model=schemas.TodoItem)
def read_item(list_id: int, item_id: int, db: Session = Depends(get_db)):
    item = crud.items.get_item(db, item_id)
    http_utils.raise_404_if_none(item, "Item not found")
    if item.list_id != list_id:
        http_utils.raise_404_if_none(None, "Item not found in this list")
    return item

@router.put("/{item_id}", response_model=schemas.TodoItem)
def update_item(list_id: int, item_id: int, item_data: schemas.TodoItemUpdate, db: Session = Depends(get_db)):
    item = crud.items.update_item(db, item_id, item_data)
    http_utils.raise_404_if_none(item, "Item not found")
    if item.list_id != list_id:
        http_utils.raise_404_if_none(None, "Item not found in this list")
    return item

@router.patch("/{item_id}/complete", response_model=schemas.TodoItem)
def complete_item(list_id: int, item_id: int, db: Session = Depends(get_db)):
    item = crud.items.complete_item(db, item_id)
    http_utils.raise_404_if_none(item, "Item not found")
    if item.list_id != list_id:
        http_utils.raise_404_if_none(None, "Item not found in this list")
    return item

@router.delete("/{item_id}", status_code=204)
def delete_item(list_id: int, item_id: int, db: Session = Depends(get_db)):
    item = crud.items.get_item(db, item_id)
    http_utils.raise_404_if_none(item, "Item not found")
    if item.list_id != list_id:
        http_utils.raise_404_if_none(None, "Item not found in this list")
    crud.items.delete_item(db, item_id)

@router.patch("/{item_id}/uncomplete", response_model=schemas.TodoItem)
def uncomplete_item(list_id: int, item_id: int, db: Session = Depends(get_db)):
    item = crud.items.uncomplete_item(db, item_id)
    http_utils.raise_404_if_none(item, "Item not found")
    if item.list_id != list_id:
        http_utils.raise_404_if_none(None, "Item not found in this list")
    return item
