def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_task(client):
    response = client.post(
        "api/v1/tasks",
        json={"title": "Test Task", "description": "This is first test task."},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Test Task"
    assert data["description"] == "This is first test task."
    assert data["done"] is False

def test_create_task_without_description(client):
    response = client.post(
        "api/v1/tasks",
        json={"title": "Only Title Task"},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Only Title Task"
    assert data["description"] == ""
    assert data["done"] is False

def test_create_task_without_title(client):
    response = client.post(
        "api/v1/tasks",
        json={"description": "This task has no title."},
    )
    assert response.status_code == 422
    data = response.json()
    assert data["detail"][0]["loc"] == ["body", "title"]
    assert data["detail"][0]["msg"] == "Field required"

def test_list_tasks_empty(client):
    response = client.get("api/v1/tasks")
    assert response.status_code == 200
    assert response.json() == []

def test_list_tasks_with_tasks(client):
    # Create two tasks first
    client.post(
        "api/v1/tasks",
        json={"title": "Task 1", "description": "First task."},
    )
    client.post(
        "api/v1/tasks",
        json={"title": "Task 2", "description": "Second task."},
    )

    response = client.get("api/v1/tasks")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["title"] == "Task 1"
    assert data[1]["title"] == "Task 2"

def test_list_tasks_with_done_filter(client):
    # Create tasks with different done statuses
    client.post(
        "api/v1/tasks",
        json={"title": "Task 1", "description": "First task."},
    )
    client.post(
        "api/v1/tasks",
        json={"title": "Task 2", "description": "Second task."},
    )
    # Mark the first task as done
    client.put("api/v1/tasks/1", json={"done": True})

    response = client.get("api/v1/tasks?done=true")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task 1"
    assert data[0]["done"] is True

    response = client.get("api/v1/tasks?done=false")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["title"] == "Task 2"
    assert data[0]["done"] is False

def test_get_task_by_id(client):
        # Create a task first
    client.post(
        "api/v1/tasks",
        json={"title": "Task 1", "description": "First task."},
    )
    client.post(
        "api/v1/tasks",
        json={"title": "Task 2", "description": "Second task."},
    )

    response = client.get("api/v1/tasks/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Task 1"
    assert data["description"] == "First task."

def test_get_task_by_id_not_found(client):
    response = client.get("api/v1/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Task not found"

def test_update_task(client):
    # Create a task first
    client.post(
        "api/v1/tasks",
        json={"title": "Task 1", "description": "First task."},
    )

    response = client.put(
        "api/v1/tasks/1",
        json={"title": "Updated Task 1", "description": "Updated description.", "done": True},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Updated Task 1"
    assert data["description"] == "Updated description."
    assert data["done"] is True

def test_update_task_not_found(client):
    response = client.put(
        "api/v1/tasks/999",
        json={"title": "Updated Task", "description": "Updated description.", "done": True},
    )
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Task not found"

def test_delete_task(client):
    # Create a task first
    client.post(
        "api/v1/tasks",
        json={"title": "Task 1", "description": "First task."},
    )

    response = client.delete("api/v1/tasks/1")
    assert response.status_code == 204

    # Verify that the task is deleted
    response = client.get("api/v1/tasks/1")
    assert response.status_code == 404

def test_delete_task_not_found(client):
    response = client.delete("api/v1/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Task not found"