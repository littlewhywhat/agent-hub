import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health_endpoint():
    """Test the /health endpoint returns OK status."""
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_health_endpoint_content_type():
    """Test the /health endpoint returns JSON content type."""
    response = client.get("/health")
    
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"