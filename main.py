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


@app.post("/todo/{todo_id}")
def update_todo(todo_id: int, title: str | None = None, details: str | None = None):
    todo = list(filter(lambda todo: todo.get("todo_id") == todo_id, fake_todos))[0]
    if title:
        todo["title"] = title
    if details:
        todo["details"] = details 
    return todo


import uuid

# generate a random UUID
my_uuid = uuid.uuid4()

# print the UUID as a string
print(str(my_uuid))
