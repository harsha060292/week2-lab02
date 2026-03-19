# 📘 Assignment: Building REST APIs with FastAPI framework

## 🎯 Objective

Learn how to build a RESTful API using FastAPI, including route definitions, data models, input validation, and automatic documentation.

## 📝 Tasks

### 🛠️ Project Setup and First Endpoint

#### Description
Initialize a FastAPI project and implement a health-check endpoint to confirm the service is running.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn (`pip install fastapi uvicorn`).
- Create `app = FastAPI()` in `starter-code.py`.
- Add a GET endpoint `/health` that returns `{"status": "ok"}`.
- Start the app with Uvicorn and confirm endpoint responds over HTTP.

### 🛠️ CRUD Endpoints for Item Resource

#### Description
Create a simple in-memory CRUD API for an `Item` resource using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model `Item` with `id: int`, `name: str`, `price: float`, and optional `description: str`.
- Implement:
  - `GET /items` (list all items)
  - `GET /items/{item_id}` (retrieve a single item)
  - `POST /items` (create item)
  - `PUT /items/{item_id}` (update item)
  - `DELETE /items/{item_id}` (remove item)
- Use an in-memory list or dictionary to store items without a database.

### 🛠️ Validation and Documentation

#### Description
Add request validation and observe auto-generated docs at `/docs`.

#### Requirements
Completed program should:

- Enforce `price` to be greater than 0 and `name` non-empty.
- Return `HTTPException(status_code=404)` for missing items.
- Use FastAPI dependency or path/query validations for query filtering (optional).
- Verify interactive API docs are available at `/docs` and `/redoc`.
