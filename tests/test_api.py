"""Unit tests for FastAPI endpoints."""

from fastapi.testclient import TestClient
from my_project.main import app
from my_project import __version__

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Welcome to my-project API"
    assert data["version"] == __version__
    assert data["documentation"] == "/docs"


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["version"] == __version__


def test_list_items():
    response = client.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert isinstance(items, list)
    assert len(items) >= 2


def test_create_and_get_item():
    payload = {
        "title": "Write unit tests",
        "description": "Ensure code reliability",
        "completed": True,
    }
    create_res = client.post("/items", json=payload)
    assert create_res.status_code == 201
    created_item = create_res.json()
    assert created_item["title"] == payload["title"]
    assert created_item["description"] == payload["description"]
    assert created_item["completed"] is True
    item_id = created_item["id"]

    # Verify retrieval
    get_res = client.get(f"/items/{item_id}")
    assert get_res.status_code == 200
    assert get_res.json() == created_item


def test_get_nonexistent_item():
    response = client.get("/items/999999")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()


def test_delete_item():
    create_res = client.post("/items", json={"title": "To be deleted"})
    assert create_res.status_code == 201
    item_id = create_res.json()["id"]

    delete_res = client.delete(f"/items/{item_id}")
    assert delete_res.status_code == 204

    # Verify deleted
    get_res = client.get(f"/items/{item_id}")
    assert get_res.status_code == 404
