# TODO: Feature 1
import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()

def test_all_movies_page(test_app):
    response = test_app.get('/movies')
    assert b'<h1>All movies</h1>' in response.data