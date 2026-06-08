"""Auth Tests"""
import pytest
from fastapi.testclient import TestClient

from src.app import app
from src.utils.database import init_db, SessionLocal, UserDB
from src.utils.security import get_password_hash

client = TestClient(app)

@pytest.fixture
def db():
    init_db()
    db = SessionLocal()
    yield db
    db.close()

def test_register_user(db):
    response = client.post("/api/v1/auth/register", json={
        "email": "test@example.com",
        "full_name": "Test User",
        "phone": "08123456789",
        "role": "buyer",
        "password": "testpassword123"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["full_name"] == "Test User"

def test_login_user(db):
    # Create user first
    db_user = UserDB(
        email="login@test.com",
        full_name="Login Test",
        phone="08123456789",
        role="buyer",
        hashed_password=get_password_hash("password123")
    )
    db.add(db_user)
    db.commit()

    response = client.post("/api/v1/auth/login", json={
        "email": "login@test.com",
        "password": "password123"
    })
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data

def test_health_check():
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
