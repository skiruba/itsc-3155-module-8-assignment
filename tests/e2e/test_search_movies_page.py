# TODO: Feature 3

import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()

def test_search_movie_page(test_app):
    response = test_app.get('/movies/search')
    assert  b'<h1 class="mb-5">Search Movie Ratings</h1>' in response.data
    assert b'<p class="mb-3">Search for a movie rating below</p>' in response.data