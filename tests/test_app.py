# tests/test_app.py

from app.main import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200

