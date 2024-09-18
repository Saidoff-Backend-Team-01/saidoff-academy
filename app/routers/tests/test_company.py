from fastapi.testclient import TestClient
import os
import pytest
from app.main import app
from app.models.banner import Banner
from fastapi_storages import FileSystemStorage, StorageFile
import io
from app.config.database import Base, engine, SessionLocal
from sqlalchemy.orm import Session

@pytest.fixture(scope="session")
def set_test_environment():
    os.environ["ENVIRONMENT"] = "testing"
    yield
    os.environ["ENVIRONMENT"] = "development"

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="module")
def client():
    return TestClient(app)



def test_banner_list(client: TestClient, db_session: Session):
    test_file = (io.BytesIO(b"abcdef"), 'test.jpg')
    db_banner = Banner(
        title="Test Banner",
        desc="test desc",
        phone_num="9989191999999",
    )
    db_session.add(db_banner)
    db_session.commit()
    db_session.refresh(db_banner)

    response = client.get("/company/banners")

    assert response.status_code == 200
    assert response.json()[0]['desc'] == 'test desc'
    assert response.json()[0]['title'] == 'Test Banner'
    assert len(response.json()) == 1



