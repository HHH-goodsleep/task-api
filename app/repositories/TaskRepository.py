from sqlalchemy import select, func

from app.database import SessionLocal
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:
    # def __init__(self):
    #     self.tasks = []
    #     self.next_id = 1

    def list_tasks(self, done: bool | None = None, limit:int = 10, offset:int = 0):
        with SessionLocal() as session:
            stmt = select(Task)
            if done is not None:
                stmt = stmt.where(Task.done == done)
            stmt = stmt.limit(limit).offset(offset)
            tasks = session.scalars(stmt).all()
            return [self._to_dict(task) for task in tasks]

    def count_tasks(self, done: bool | None = None):
        with SessionLocal() as session:
            stmt = select(func.count()).select_from(Task)
            if done is not None:
                stmt = stmt.where(Task.done == done)
            return session.scalar(stmt)
        
    def get_task(self, task_id: int):
        with SessionLocal() as session:
            task = session.get(Task, task_id)
            return self._to_dict(task) if task else None

    def create_task(self, data: TaskCreate):
        with SessionLocal() as session:
            task = Task(title=data.title, description=data.description, done=False)
            session.add(task)
            session.commit()
            session.refresh(task)
            return self._to_dict(task)
        
    def update_task(self, task_id: int, data: TaskUpdate):
        with SessionLocal() as session:
            task = session.get(Task, task_id)
            if not task:
                return None
            if data.title is not None:
                task.title = data.title
            if data.description is not None:
                task.description = data.description
            if data.done is not None:
                task.done = data.done
            session.commit()
            session.refresh(task)
            return self._to_dict(task)

    def delete_task(self, task_id: int):
        with SessionLocal() as session:
            task = session.get(Task, task_id)
            if not task:
                return False
            session.delete(task)
            session.commit()
            return True


    @staticmethod
    def _to_dict(task: Task):
        return {
            "id": task.id,
            "title": task.title,
            "description": task.description,
            "done": task.done,
        }

# 全项目共享的唯一仓储实例：create / list / update 都读写同一份 tasks
task_repository = TaskRepository()