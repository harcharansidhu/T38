# SE T38 - Semantic Similarity (NLP)
# Compulsory Task 2

# IMPORTS
import spacy

# Specify the language model
nlp = spacy.load('en_core_web_md')

# Load the movie recommendation data
# path to movie text file:
path = "./T38/movies.txt"

# init list of movies to recommended from
movies = []
# read in movie list
with open(path, 'r') as f:
    for line in f:
        # split the movie name from description
        line = map(lambda txt: txt.strip(), line.split(':',1))
        movies.append(list(line))

# 
def movie_recommender(description):
    """
    Movie recommender function
    INPUT: 
        the description of the movie to compare against to, 
    OUTPUT:
        recommend a movie with the highest similarity score 
    """
    # initial variables
    movie_to_recommend = "No movie recommended"
    similarity_score = -1

    # find the movie with the highest similarity score by looping over the movies list
    token = nlp(description)
    for movie_title, movie_description in movies:
        # Get similarity score
        token_ = nlp(movie_description)
        score = token.similarity(token_)
        
        # update variables with a higher similarity score
        if score > similarity_score:
            similarity_score = score
            movie_to_recommend = movie_title
    
    return movie_to_recommend