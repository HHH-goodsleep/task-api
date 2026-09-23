from fastapi import FastAPI

from app.api import tasks

app = FastAPI(title="Task Management API", version="1.0.0")

app.include_router(tasks.router)

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

