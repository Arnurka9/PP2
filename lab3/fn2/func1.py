"""
Write a function that takes a single movie and returns True if its IMDB score is above 5.5
"""

def good_movie(movies, movie_name):
    for movie in movies:
        if movie["imdb"] > 5.5 and movie_name == movie["name"]:
            return True
        return False