
def movies_by_category(movies, category):
    category_movies = []
    for movie in movies:
        if movie["category"] == category:
            category_movies.append(movie["name"])
    
    return category_movies