from fastapi import FastAPI

from app.api import tasks
from app.database import init_db

init_db()

app = FastAPI(title="Task Management API", version="1.0.0")

app.include_router(tasks.router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Welcome to the Task Management API!", "docs": "/docs"}

