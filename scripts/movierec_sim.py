import sys
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
from scipy.sparse import csr_matrix
import time

# Ensure clean output by removing unnecessary print statements
selected_ids = list(map(int, sys.argv[1:]))

# Start timing
start_time = time.time()

# Load data
ratings_data = pd.read_csv("./data/ratings.csv")
movie_data = pd.read_csv("./data/movies.csv")

# Compute average ratings
avg_ratings = ratings_data.groupby("movieId")["rating"].mean().reset_index()

# Merge ratings into movie data
movie_data = movie_data.merge(avg_ratings, on="movieId", how="left")

# Create a user-movie matrix
user_movie_matrix = ratings_data.pivot(index="userId", columns="movieId", values="rating").fillna(0)
sparse_matrix = csr_matrix(user_movie_matrix)

# Compute similarity matrix (using Dense Output)
similarity_matrix = cosine_similarity(sparse_matrix.T)

# Get recommendations
recommendations = {}
for movie_id in selected_ids:
    if movie_id in user_movie_matrix.columns:
        movie_index = user_movie_matrix.columns.get_loc(movie_id)
        similar_movies = list(enumerate(similarity_matrix[movie_index]))
        similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:11]

        for sim_movie_id, score in similar_movies:
            actual_movie_id = user_movie_matrix.columns[sim_movie_id]
            recommendations[actual_movie_id] = score

# Sort recommendations by similarity score
recommended_movie_ids = sorted(recommendations, key=recommendations.get, reverse=True)[:10]

# Get recommended movie details
recommended_movies = movie_data[movie_data["movieId"].isin(recommended_movie_ids)]

# Prepare the recommendations as a list of dictionaries
recommended_movies_list = recommended_movies.to_dict(orient='records')

# Print only the JSON output
print(json.dumps(recommended_movies_list, ensure_ascii=False))

# Timing and performance
#print(f"Processing Time: {time.time() - start_time} seconds")
