from fastapi import APIRouter

from app.services.task_services import TaskService
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/api/v1/tasks", tags=["tasks"])

@router.get("", response_model=list[TaskResponse])
def list_tasks(done: bool | None = None):
    return TaskService().list_tasks(done)

@router.get("/{task_id}", response_model=TaskResponse)
def get_task(task_id: int):
    return TaskService().get_task(task_id)

@router.post("", response_model=TaskResponse, status_code=201)
def create_task(data: TaskCreate):
    return TaskService().create_task(data)

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, data: TaskUpdate):
    return TaskService().update_task(task_id, data)

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int):
    TaskService().delete_task(task_id)