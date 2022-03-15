# TODO: Feature 2
from src.repositories.movie_repository import movie_repository_singleton
from src.models.movie import Movie


def test_create_movies_form():
    movie = movie_repository_singleton.create_movie('The Dark Knight', 'Christopher Nolan', 4)

    assert type(movie) == Movie
    assert movie.title == 'The Dark Knight'
    assert movie.director == 'Christopher Nolan'
    assert movie.rating == 4
    
