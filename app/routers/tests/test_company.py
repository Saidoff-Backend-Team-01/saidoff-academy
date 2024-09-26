from fastapi.testclient import TestClient
import os
import pytest
from app.main import app
from app.models.banner import Banner
from app.models.why_we_us import WhyWeUs
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


def test_banner_single(client: TestClient, db_session: Session):
    test_file = (io.BytesIO(b"abcdef"), 'test.jpg')
    db_banner = Banner(
        title="Test Banner_Single",
        desc="test desc_single",
        phone_num="998911000000",
    )
    db_session.add(db_banner)
    db_session.commit()
    db_session.refresh(db_banner)

    response = client.get(f"/company/banners/{db_banner.id}")

    assert response.status_code == 200
    data = response.json()

    assert data['desc'] == 'test desc_single'
    assert data['title'] == 'Test Banner_Single'


def test_why_we_us_list(client: TestClient, db_session: Session):
    test_file = (io.BytesIO(b"abcdef"), 'test.jpg')
    db_why_we_us = [
        WhyWeUs(title="Reason 1", desc="Description 1"),
        WhyWeUs(title="Reason 2", desc="Description 2"),
        WhyWeUs(title="Reason 3", desc="Description 3"),
        WhyWeUs(title="Reason 4", desc="Description 4"),
    ]
    db_session.add_all(db_why_we_us)
    db_session.commit()
    db_session.refresh(db_why_we_us)
    response = client.get("/why_we_us/")

    assert response.status_code == 200
    data = response.json()

    assert len(data) == 3
    assert data[0]['title'] == 'Reason 4'
    assert data[1]['title'] == 'Reason 3'
    assert data[2]['title'] == 'Reason 2'
