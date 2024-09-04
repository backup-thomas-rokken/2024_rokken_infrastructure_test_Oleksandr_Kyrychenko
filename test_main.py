from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import app, get_db, Base

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_todo():
    response = client.post(
        "/todos/",
        json={"title": "Test todo", "description": "This is a test"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test todo"
    assert data["description"] == "This is a test"
    assert "id" in data

def test_read_todos():
    response = client.get("/todos/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0

def test_read_todo():
    # First, create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Test todo for reading", "description": "This is a test"}
    )
    created_todo = create_response.json()

    # Then, read the created todo
    response = client.get(f"/todos/{created_todo['id']}")
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test todo for reading"
    assert data["description"] == "This is a test"

def test_update_todo():
    # First, create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Test todo for updating", "description": "This is a test"}
    )
    created_todo = create_response.json()

    # Then, update the created todo
    update_response = client.put(
        f"/todos/{created_todo['id']}",
        json={"title": "Updated test todo", "description": "This is an updated test"}
    )
    assert update_response.status_code == 200
    updated_todo = update_response.json()
    assert updated_todo["title"] == "Updated test todo"
    assert updated_todo["description"] == "This is an updated test"

def test_delete_todo():
    # First, create a todo
    create_response = client.post(
        "/todos/",
        json={"title": "Test todo for deleting", "description": "This is a test"}
    )
    created_todo = create_response.json()

    # Then, delete the created todo
    delete_response = client.delete(f"/todos/{created_todo['id']}")
    assert delete_response.status_code == 200

    # Verify that the todo has been deleted
    get_response = client.get(f"/todos/{created_todo['id']}")
    assert get_response.status_code == 404