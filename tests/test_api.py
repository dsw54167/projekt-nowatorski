from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_app_starts():
    response = client.get("/docs")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}