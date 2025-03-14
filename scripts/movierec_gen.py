import sys
import pandas as pd
import json

genre = sys.argv[1]  # Genre as a string

# Load movie data
movies_data = pd.read_csv("./data/movies.csv")
ratings_data = pd.read_csv("./data/ratings.csv")  # Load ratings

# Compute average rating per movie
avg_ratings = ratings_data.groupby("movieId")["rating"].mean().reset_index()

# Merge ratings into movies data
movies_data = movies_data.merge(avg_ratings, on="movieId", how="left")

# Filter movies by genre
movies_by_genre = movies_data[movies_data['genres'].str.contains(genre, case=False, na=False)]

if movies_by_genre.empty:
    print(json.dumps([]))  # Return empty list as JSON
else:
    movies_list = movies_by_genre[['movieId', 'title', 'genres', 'rating']].to_dict(orient='records')
    print(json.dumps(movies_list))  # Return movie list as JSON
