from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import subprocess
import os
import json
import pandas as pd

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session handling

# Ensure the scripts folder is found
SCRIPTS_DIR = os.path.join(os.path.dirname(__file__), "scripts")

# Load movie data
movies_data = pd.read_csv("./data/movies.csv")

# Extract unique years from the dataset
movies_data["year"] = movies_data["title"].str.extract(r"\((\d{4})\)").astype("Int64")
unique_years = sorted(movies_data["year"].dropna().unique().tolist())

# Extract unique genres from the dataset
unique_genres = sorted(set(genre for sublist in movies_data["genres"].str.split('|').dropna() for genre in sublist))


@app.route('/')
def home():
    return render_template('home.html', years=unique_years, genres=unique_genres)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/output', methods=['POST'])
def output():
    movies = []

    if 'button1' in request.form:
        year = request.form.get("dropdown1")
        result = subprocess.run(
            ["python", os.path.join(SCRIPTS_DIR, "movierec.py"), year],
            capture_output=True, text=True, encoding="utf-8"
        )
        movies = json.loads(result.stdout)

    elif 'button2' in request.form:
        genre = request.form.get("dropdown2")
        result = subprocess.run(
            ["python", os.path.join(SCRIPTS_DIR, "movierec_gen.py"), genre],
            capture_output=True, text=True, encoding="utf-8"
        )
        movies = json.loads(result.stdout)

    # Sort movies by rating in descending order
    movies = sorted(movies, key=lambda x: x['rating'], reverse=True)

    return render_template("output.html", movies=movies)


@app.route('/recommend_more', methods=['POST'])
def recommend_more():
    watched_movie_ids = request.form.getlist('watched_movies')

    if not watched_movie_ids:
        return "⚠️ Please select at least one movie!"

    # Run the recommendation script with selected movie IDs
    result = subprocess.run(
        ["python", os.path.join(SCRIPTS_DIR, "movierec_sim.py")] + watched_movie_ids,
        capture_output=True, text=True, encoding="utf-8"
    )
    print("📌 Script Output:", result.stdout)
    print("❌ Script Error:", result.stderr)

    # Parse the recommendations JSON output from the script
    recommendations = json.loads(result.stdout)

    # Sort movies by rating in descending order
    recommendations = sorted(recommendations, key=lambda x: x['rating'], reverse=True)

    return render_template("recommend.html", recommendations=recommendations)





@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
