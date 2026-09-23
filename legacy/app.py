from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None

tasks = []

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/api/v1/tasks")
def list_tasks(done: bool | None = None):
    if done is None:
        return tasks
    return [task for task in tasks if task["done"] == done]

@app.get("/api/v1/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/api/v1/tasks", status_code=201)
def create_task(data: TaskCreate):
    task = {
        "id": len(tasks) + 1,
        "title": data.title,
        "description": data.description,
        "done": False,
    }
    tasks.append(task)
    return task

@app.put("/api/v1/tasks/{task_id}")
def update_task(task_id: int, data: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            if data.title is not None:
                task["title"] = data.title
            if data.description is not None:
                task["description"] = data.description
            if data.done is not None:
                task["done"] = data.done
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/api/v1/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(i)
            return
    raise HTTPException(status_code=404, detail="Task not found")