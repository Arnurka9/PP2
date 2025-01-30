
def avg_IMDB(movies):
    gemeral_score = 0
    count_movies = 0
    
    for movie in movies:
        gemeral_score += movie["imdb"]
        count_movies += 1
    
    return gemeral_score/count_movies
        