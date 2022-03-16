# TODO: Feature 3
# TODO: Feature 3
from src.repositories.movie_repository import movie_repository_singleton

def test_search():
    movie = movie_repository_singleton.create_movie('Batman Begins', 'Christopher Nolan', 4)
    assert movie.title == 'Batman Begins'
    assert movie.director == 'Christopher Nolan'
    assert movie.rating == 4

    movie = movie_repository_singleton.create_movie('The Dark Knight', 'Christopher Nolan', 1)
    assert movie.title == 'The Dark Knight'
    assert movie.director == 'Christopher Nolan'
    assert movie.rating == 1

    movie = movie_repository_singleton.create_movie('The Dark Knight Rises', 'Christopher Nolan', 2)
    assert movie.title == 'The Dark Knight Rises'
    assert movie.director == 'Christopher Nolan'
    assert movie.rating == 2