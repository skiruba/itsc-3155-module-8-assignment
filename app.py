from flask import Flask, redirect, render_template
from src.repositories.movie_repository import movie_repository_singleton

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')


@app.get('/movies')
def list_all_movies():
    # TODO: Feature 1
    return render_template('list_all_movies.html', list_movies_active=True)


@app.get('/movies/new')
def create_movies_form():
    return render_template('create_movies_form.html', create_rating_active=True)


@app.post('/movies')
def create_movie():
    # TODO: Feature 2
    # After creating the movie in the database, we redirect to the list all movies page
    return redirect('/movies')


@app.get('/movies/search')
def search_movies():
    # TODO: Feature 3
    
    movie_list = []
    movies = request.args.get("movie_name")
    movie_list = movie_repository_singleton.get_movie_by_title(movies)
    error = " "
    if movies != None:
        result = "The movies name is " + movie_list.title + " and is directed by " + movie_list.director + " has a rating of " + movie_list.rating + "."
    if movie_list == None and movies != None:
        error = "No movie found"
        result = ""
    if movies == None:
        result = ""
    return render_template('search_movies.html', search_active=True, result = result, error = error)