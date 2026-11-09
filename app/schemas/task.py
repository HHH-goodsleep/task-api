from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str
    description: str = ""

class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    done: bool | None = None

class TaskResponse(BaseModel):
    id: int
    title: str
    description: str
    done: bool

class TaskListResponse(BaseModel):
    items: list[TaskResponse]
    total: int
    limit: int
    offset: int

    