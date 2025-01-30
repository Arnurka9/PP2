
def avg_IMDB_by_category(movies, category):
    gemeral_score = 0
    count_movies = 0
    
    for movie in movies:
        if category == movie["category"]:
            gemeral_score += movie["imdb"]
            count_movies += 1
    
    return gemeral_score/count_movies
        