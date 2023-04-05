from fastapi import FastAPI


app = FastAPI(
    title="Todo app"
)


fake_todos = [
    {"todo_id": 101, "title": "Test title 1", "details": "Test details 1"},
    {"todo_id": 102, "title": "Test title 2", "details": "Test details 2"},
    {"todo_id": 103, "title": "Test title 3", "details": "Test details 3"},
]


@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    return [todo for todo in fake_todos if todo.get("todo_id") == todo_id]


@app.get("/todos")
def get_todos(limit: int, offset: int):
    return fake_todos[offset:][:limit]
