import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.database import Base, engine 

@pytest.fixture
def client():
    return TestClient(app)



@pytest.fixture(autouse=True)
def reset_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)