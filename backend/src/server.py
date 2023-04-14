from typing import Annotated, List
from fastapi import FastAPI, Query
from pydantic import BaseModel, Field
from src.api.schemas.todo import Todo
import uuid



api = FastAPI(
    title="Todo app"
)


fake_todos = [
    Todo(id = "stringstringstringstringstringstringstringstring1", title = "Test title 1", details = "Test details 1", isComplete = True),
    Todo(id = "stringstringstringstringstringstringstringstring2", title = "Test title 2", details = "Test details 2", isComplete = False),
    Todo(id = "stringstringstringstringstringstringstringstring3", title = "Test title 3", details = "Test details 3", isComplete = False)
]


@api.get("/todo/{id}")
def get_todo(id: int):
    return [todo for todo in fake_todos if todo.get("id") == id]


@api.get("/todos", response_model=List[Todo])
def get_todos(limit: int, offset: int):
    return fake_todos[offset:][:limit]


@api.post("/todos")
def add_todos(todos: List[Todo]):
    fake_todos.extend(todos)
    return {"status": 200, "data": fake_todos}
