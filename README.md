# FastAPI Todo Application

This application allows you to manage a simple list of todos. The data will be stored in **RAM** of the application and will be kept during the application's runtime.

## I. Setup enviroment

1. Create env

```
python3 -m venv venv
source venv/bin/activate
```

2. Install FastAPI and Uvicorn
   First, install the required dependencies, FastAPI and Uvicorn (ASGI server to run FastAPI).

```
pip install fastapi uvicorn
```

## II. Explanation

- Storing in RAM: The todos list is used to store todo items in memory.

- Todo Schema: The Todo class defines the structure of a todo, with fields title, description, and completed.

- API Endpoints:

    - GET /todos: Returns a list of all todos.

    - POST /todos: Adds a new todo to the list.

    - GET /todos/{todo_id}: Fetches a specific todo by its todo_id.

## Run application

```
uvicorn main:app --reload
```

### 1. GET /todos

```
curl -X 'GET' 'http://127.0.0.1:8000/todos'
```

### 2. POST /todos

```
curl -X 'POST' \
  'http://127.0.0.1:8000/todos' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "Learn FastAPI",
  "description": "Learn how to use FastAPI to create a simple API",
  "completed": false
}'
```

### 3. GET /todos/{todo_id}

```
curl -X 'GET' 'http://127.0.0.1:8000/todos/1'
```

