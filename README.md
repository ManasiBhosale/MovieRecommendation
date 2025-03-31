# Movie Recommendation System

This project is a Movie Recommendation System that suggests movies based on user preferences and viewing history. Built with Flask, it provides an interactive web interface for users to receive personalized movie recommendations.

## Features

- **User Interaction**: Users can input their watched movies to receive tailored recommendations.
- **Data-Driven Suggestions**: Utilizes the MovieLens dataset to generate accurate recommendations.
- **Web Interface**: A simple and intuitive web interface built with Flask.

## Dataset

The system employs the [MovieLens](https://grouplens.org/datasets/movielens/) dataset, which includes:

- **Ratings Data**: User ratings for various movies.
- **Movies Data**: Details about movies such as titles and genres.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/ManasiBhosale/MovieRecommendation.git
   ```


2. **Navigate to the Project Directory**:

   ```bash
   cd MovieRecommendation
   ```


3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```


4. **Download the Dataset**:

   Place the MovieLens dataset files (`ratings.csv`, `movies.csv`, etc.) into the `data` directory.

## Usage

1. **Start the Flask Application**:

   ```bash
   python app.py
   ```


2. **Access the Web Interface**:

   Open a web browser and navigate to `http://127.0.0.1:5000/`.

3. **Get Recommendations**:

   Select or input movies you've watched, and the system will provide personalized recommendations.

## Project Structure

- **`app.py`**: Main Flask application file.
- **`data/`**: Directory containing the dataset files.
- **`scripts/`**: Contains scripts for data processing and recommendation algorithms.
- **`templates/`**: HTML templates for the web interface.
- **`static/styles/`**: CSS stylesheets for the web interface.
- **`requirements.txt`**: List of Python dependencies.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

Special thanks to the [MovieLens](https://grouplens.org/datasets/movielens/) project for providing the dataset used in this system.
