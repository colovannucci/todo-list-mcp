from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.dependencies import get_db
from app.utils import http as http_utils

router = APIRouter(prefix="/lists", tags=["lists"])

@router.post("/", response_model=schemas.TodoList)
def create_list(list_data: schemas.TodoListCreate, db: Session = Depends(get_db)):
    return crud.lists.create_list(db, list_data)

@router.get("/{list_id}", response_model=schemas.TodoList)
def read_list(list_id: int, db: Session = Depends(get_db)):
    list_ = crud.lists.get_list(db, list_id)
    http_utils.raise_404_if_none(list_, "List not found")
    return list_

@router.put("/{list_id}", response_model=schemas.TodoList)
def update_list(list_id: int, list_data: schemas.TodoListUpdate, db: Session = Depends(get_db)):
    list_ = crud.lists.update_list(db, list_id, list_data)
    http_utils.raise_404_if_none(list_, "List not found")
    return list_

@router.delete("/{list_id}", status_code=204)
def delete_list(list_id: int, db: Session = Depends(get_db)):
    deleted = crud.lists.delete_list(db, list_id)
    http_utils.raise_404_if_none(deleted, "List not found")

@router.get("/{list_id}/items/all", response_model=list[schemas.TodoItem])
def read_items_for_list(list_id: int, db: Session = Depends(get_db)):
    list_ = crud.lists.get_list(db, list_id)
    http_utils.raise_404_if_none(list_, "List not found")
    return crud.items.get_items_for_list(db, list_id)

@router.get("/", response_model=list[schemas.TodoList])
def read_all_lists(db: Session = Depends(get_db)):
    lists = crud.lists.get_all_lists(db)
    return lists
