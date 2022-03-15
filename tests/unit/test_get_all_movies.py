# TODO: Feature 1
# Recieved help from Michael Pearce
from flask import Flask
import pytest, unittest
from src.repositories import movie_repository
from src.repositories.movie_repository import MovieRepository

def test_get_all_movies():
    temp = MovieRepository()
    temp_list = MovieRepository.get_all_movies(self=temp)
    assert len(temp_list) == 0
    temp.create_movie("Batman Begins", "Christopher Nolan", 5)
    temp_list = MovieRepository.get_all_movies(self=temp)
    assert len(temp_list) == 1
    temp.create_movie("The Dark Knight", "Christopher Nolan", 5)
    temp.create_movie("The Dark Knight Rises", "Christopher Nolan", 5)
    temp_list = MovieRepository.get_all_movies(self=temp)
    assert len(temp_list) == 3