import sys
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import json
sys.stdout.reconfigure(encoding='utf-8')

selected_ids = list(map(int, sys.argv[1:]))
#print(f"🎯 Selected movie IDs: {selected_ids}")

# Load data
#print("📂 Loading data...")
ratings_data = pd.read_csv("./data/ratings.csv")
movie_data = pd.read_csv("./data/movies.csv")
#print("✅ Data loaded!")

# Compute average ratings
avg_ratings = ratings_data.groupby("movieId")["rating"].mean().reset_index()

# Merge ratings into movie data
movie_data = movie_data.merge(avg_ratings, on="movieId", how="left")

# Create a user-movie matrix
user_movie_matrix = ratings_data.pivot(index="userId", columns="movieId", values="rating").fillna(0)

# Compute similarity matrix
#print("🔢 Calculating movie similarities...")
similarity_matrix = cosine_similarity(user_movie_matrix.T)
sim_df = pd.DataFrame(similarity_matrix, index=user_movie_matrix.columns, columns=user_movie_matrix.columns)

# Get recommendations
recommendations = {}
for movie_id in selected_ids:
    similar_movies = sim_df[movie_id].sort_values(ascending=False)[1:11]  # Top 5 similar movies
    for sim_movie_id, score in similar_movies.items():
        recommendations[sim_movie_id] = score

# Sort recommendations by similarity score
recommended_movie_ids = sorted(recommendations, key=recommendations.get, reverse=True)[:10]

# Get recommended movie details
recommended_movies = movie_data[movie_data["movieId"].isin(recommended_movie_ids)]

# Prepare the recommendations as a list of dictionaries
recommended_movies_list = recommended_movies.to_dict(orient='records')

# Return recommendations as JSON
#print("✅ Recommendations prepared!")
print(json.dumps(recommended_movies_list, ensure_ascii=False))
sys.stdout.flush()

