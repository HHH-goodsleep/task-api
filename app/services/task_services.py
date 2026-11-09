from fastapi import HTTPException

from app.repositories.TaskRepository import task_repository
from app.schemas.task import TaskCreate, TaskUpdate

class TaskService:
    def list_tasks(self, done: bool | None = None, limit: int = 10, offset: int = 0):
        items = task_repository.list_tasks(done, limit, offset)
        total = task_repository.count_tasks(done)
        return {
            "items": items,
            "total": total,
            "limit": limit,
            "offset": offset,
        }

    def get_task(self, task_id: int):
        task = task_repository.get_task(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task

    def create_task(self, data: TaskCreate):
        return task_repository.create_task(data)

    def update_task(self, task_id: int, data: TaskUpdate):
        task = task_repository.get_task(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task_repository.update_task(task_id, data)

    def delete_task(self, task_id: int):
        task = task_repository.get_task(task_id)
        if task is None:
            raise HTTPException(status_code=404, detail="Task not found")
        return task_repository.delete_task(task_id)