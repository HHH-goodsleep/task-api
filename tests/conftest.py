import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.repositories.TaskRepository import task_repository

@pytest.fixture
def client():
    return TestClient(app)



@pytest.fixture(autouse=True)
def reset_task_repository():
    task_repository.tasks.clear()
    task_repository.next_id = 1
    yield
    task_repository.tasks.clear()
    task_repository.next_id = 1
    