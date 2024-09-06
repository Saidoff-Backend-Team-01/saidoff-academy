from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_banner_list():
    response = client.get("/banners/")
    print(response.json())
    assert response.status_code == 404