from app.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def list_tasks(self, done: bool | None = None):
        if done is None:
            return self.tasks
        return [task for task in self.tasks if task["done"] == done]

    def get_task(self, task_id: int):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def create_task(self, data: TaskCreate):
        task = {
            "id": self.next_id,
            "title": data.title,
            "description": data.description,
            "done": False,
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def update_task(self, task_id: int, data: TaskUpdate):
        task = self.get_task(task_id)
        if task is None:
            return None
        if data.title is not None:
            task["title"] = data.title
        if data.description is not None:
            task["description"] = data.description
        if data.done is not None:
            task["done"] = data.done
        return task

    def delete_task(self, task_id: int):
        task = self.get_task(task_id)
        if task is None:
            return False
        self.tasks.remove(task)
        return True


# 全项目共享的唯一仓储实例：create / list / update 都读写同一份 tasks
task_repository = TaskRepository()