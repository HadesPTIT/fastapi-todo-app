from fastapi import FastAPI, HTTPException
from typing import List
from models import Todo

app = FastAPI()

# Giả lập database bằng danh sách trong RAM
todos: List[Todo] = []

@app.get("/")
async def root():
    return {"message": "Welcome to the To-Do API"}

@app.get("/todos", response_model=List[Todo])
async def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=Todo)
async def create_todo(todo: Todo):
    for existing in todos:
        if existing.id == todo.id:
            raise HTTPException(status_code=400, detail="ID already exists")
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")
