import pytest
from test_db import client, create_test_db

@pytest.fixture(scope="module", autouse=True)
def setup_db():
    create_test_db()

def test_add_product():
    response = client.post("/products/", json={
        "name": "Test Product",
        "price": 19.99,
        "description": "Opis testowy"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Test Product"
    assert data["price"] == 19.99
    assert data["description"] == "Opis testowy"

