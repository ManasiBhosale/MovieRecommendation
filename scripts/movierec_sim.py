import sys
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
from scipy.sparse import csr_matrix

sys.stdout.reconfigure(encoding='utf-8')

selected_ids = list(map(int, sys.argv[1:]))

# Load data with optimized memory usage
ratings_data = pd.read_csv(
    "./data/ratings.csv", 
    usecols=["userId", "movieId", "rating"], 
    dtype={"userId": np.int32, "movieId": np.int32, "rating": np.float32}
)
movie_data = pd.read_csv(
    "./data/movies.csv", 
    usecols=["movieId", "title"], 
    dtype={"movieId": np.int32, "title": str}
)

# Compute average ratings and merge
avg_ratings = ratings_data.groupby("movieId", as_index=False)["rating"].mean()
movie_data = movie_data.merge(avg_ratings, on="movieId", how="left")

# Create a sparse user-movie matrix directly
user_movie_matrix = ratings_data.pivot_table(
    index="userId", columns="movieId", values="rating", fill_value=0
)
sparse_matrix = csr_matrix(user_movie_matrix.values)

# Compute sparse similarity matrix
similarity_matrix = cosine_similarity(sparse_matrix.T, dense_output=False)

# Precompute movie ID to column index mapping
movie_id_to_col = {movie_id: idx for idx, movie_id in enumerate(user_movie_matrix.columns)}

# Get recommendations
recommendations = {}
for movie_id in selected_ids:
    col_idx = movie_id_to_col.get(movie_id)
    if col_idx is not None:
        similar_movies = similarity_matrix[col_idx].toarray().flatten()
        top_similar = np.argsort(similar_movies)[::-1][1:11]  # Exclude self and get top 10
        
        for sim_idx in top_similar:
            actual_movie_id = user_movie_matrix.columns[sim_idx]
            score = similar_movies[sim_idx]
            recommendations[actual_movie_id] = score

# Sort recommendations by similarity score
recommended_movie_ids = sorted(recommendations, key=recommendations.get, reverse=True)[:10]

# Get recommended movie details
recommended_movies = movie_data[movie_data["movieId"].isin(recommended_movie_ids)]

# Prepare the recommendations as a list of dictionaries
recommended_movies_list = recommended_movies.to_dict(orient='records')

# Return recommendations as JSON
print(json.dumps(recommended_movies_list, ensure_ascii=False))
sys.stdout.flush()
