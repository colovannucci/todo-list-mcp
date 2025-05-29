from pydantic import BaseModel

# --- Todo List Schemas ---

class TodoListBase(BaseModel):
    name: str

class TodoListCreate(TodoListBase):
    pass

class TodoListUpdate(BaseModel):
    name: str | None = None

class TodoList(TodoListBase):
    id: int

    class Config:
        orm_mode = True

# --- Todo Item Schemas ---

class TodoItemBase(BaseModel):
    title: str
    description: str | None = None

class TodoItemCreate(TodoItemBase):
    pass

class TodoItemUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None

class TodoItem(TodoItemBase):
    id: int
    list_id: int
    completed: bool = False

    class Config:
        orm_mode = True
