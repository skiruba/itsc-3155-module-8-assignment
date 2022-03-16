# TODO: Feature 2
from src.repositories.movie_repository import movie_repository_singleton, MovieRepository


def test_create_movie():
        #create 3 movie instances

        M1 = movie_repository_singleton.create_movie('Spider Man', 'Stan Lee', 4)

        # check if all attributes are correct
        assert M1.title == 'Spider Man'
        assert M1.director == 'Stan Lee'
        assert M1.rating == 4
        # check if movie is in respository
        assert M1 in movie_repository_singleton._db

        M2 = movie_repository_singleton.create_movie('Lord of The Rings', 'JRR Tolkien', 5)
        
        # check if all attributes are correct
        assert M2.title == 'Lord of The Rings'
        assert M2.director == 'JRR Tolkien'
        assert M2.rating == 5
        # check if movie is in respository
        assert M2 in movie_repository_singleton._db

        M3 = movie_repository_singleton.create_movie('Forrest Gump', 'Robert Zemeckis', 5)


        # check if all attributes are correct
        assert M3.title == 'Forrest Gump'
        assert M3.director == 'Robert Zemeckis'
        assert M3.rating == 5
        # check if movie is in respository
        assert M3 in movie_repository_singleton._db







