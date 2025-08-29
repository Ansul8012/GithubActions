import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Simple Calculator' in response.data


def test_add(client):
    response = client.post('/calculate', json={'a': 2, 'b': 3, 'op': 'add'})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5


def test_sub(client):
    response = client.post('/calculate', json={'a': 5, 'b': 2, 'op': 'sub'})
    assert response.status_code == 200
    assert response.get_json()['result'] == 3


def test_mul(client):
    response = client.post('/calculate', json={'a': 4, 'b': 3, 'op': 'mul'})
    assert response.status_code == 200
    assert response.get_json()['result'] == 12


def test_div(client):
    response = client.post('/calculate', json={'a': 10, 'b': 2, 'op': 'div'})
    assert response.status_code == 200
    assert response.get_json()['result'] == 5.0


def test_div_zero(client):
    response = client.post('/calculate', json={'a': 10, 'b': 0, 'op': 'div'})
    assert response.status_code == 200
    assert response.get_json()['result'] == 'Error: Division by zero'
