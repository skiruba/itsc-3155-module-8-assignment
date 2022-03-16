# TODO: Feature 2
from urllib import response
import pytest
from app import app

@pytest.fixture()
def test_app():
    return app.test_client()

def test_create_movie_page(test_app):

    
    response = test_app.get('/movies/new')
    assert b'<h1 class="mb-5">Create Movie Rating</h1>' in response.data
    assert b'<p class="mb-3">Create a movie rating below</p>' in response.data
    assert b'<form action="/movies" method="post">' in response.data
    assert b'<button type="submit" class="btn btn-primary">Submit</button>' in response.data



