# TODO: Feature 1
import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()

def test_all_movies_page(test_app):
    response = test_app.get('/movies')
    assert b'<h1 class="mb-5">All Movies</h1>' in response.data
    assert b'<p class="mb-3">See our list of movie ratings below</p>' in response.data
    assert b'<th>Movie</th>' in response.data
    assert b'<th>Director</th>' in response.data
    assert b'<th>Rating</th>' in response.data