import sys
import pandas as pd
import json

year = sys.argv[1]  # Year as a string

# Database connection settings (not used in this version)
# db_config = { ... }

# Load movie data
movies_data = pd.read_csv("./data/movies.csv")
ratings_data = pd.read_csv("./data/ratings.csv")  # Load ratings

# Compute average rating per movie
avg_ratings = ratings_data.groupby("movieId")["rating"].mean().reset_index()

# Merge ratings into movies data
movies_data = movies_data.merge(avg_ratings, on="movieId", how="left")

# Filter movies by year
movies_by_year = movies_data[movies_data['title'].str.contains(f"\\({year}\\)", case=False, na=False, regex=True)]

if movies_by_year.empty:
    print(json.dumps([]))  # Return empty list as JSON
else:
    movies_list = movies_by_year[['movieId', 'title', 'genres', 'rating']].to_dict(orient='records')
    print(json.dumps(movies_list))  # Return movie list as JSON
