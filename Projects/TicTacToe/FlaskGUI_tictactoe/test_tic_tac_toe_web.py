# test_tic_tac_toe_web.py
import pytest
from tic_tac_toe_web import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Tic Tac Toe" in response.data

def test_make_move(client):
    client.post('/move', data={'row': 0, 'col': 0})
    response = client.get('/')
    assert response.status_code == 200
    assert b"X" in response.data