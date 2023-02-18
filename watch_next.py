# SE T38 - Semantic Similarity (NLP)
# Compulsory Task 2

# IMPORTS
# language model library
import spacy
# table making library
from tabulate import tabulate

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

# Set up variables to specify watched movie
movie_watched = "Planet Hulk"
movie_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# get a movie recommendation based on movie watched
movie_recommendation = movie_recommender(movie_description)

# Print summary
summary = []
summary.append(["Movie watched", movie_watched])
summary.append(["Movie description", movie_description])
summary.append(["Movie recommended", movie_recommendation])

print(tabulate(summary, tablefmt="simple_grid", maxcolwidths=[None, 50]))
