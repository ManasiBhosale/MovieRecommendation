# Movie Recommendation System

This project is a Movie Recommendation System that suggests movies based on user preferences and viewing history. Built with Flask, it provides an interactive web interface for users to receive personalized movie recommendations.

## Features

- **User Interaction**: Users can input their watched movies to receive tailored recommendations.
- **Data-Driven Suggestions**: Utilizes the MovieLens dataset to generate accurate recommendations.
- **Web Interface**: A simple and intuitive web interface built with Flask.
- **Recommendation Flexibility**: Users can choose movies based on genre or year.

## How Recommendations are Made

The recommendation process in this system works as follows:

1. **User Input (Genre/Year)**:  
   Users begin by selecting a genre or a year to filter the movies. The system displays a set of movies that match the chosen criteria.  

2. **Watched Movie Selection**:  
   Users then pick movies they have already watched from the filtered list. This helps the system understand the user's preferences.  

3. **Recommendation Generation**:  
   After the user selects their watched movies, the system generates recommendations using the following approach:  

   - **Data Preparation**:  
     The system reads the ratings data (`ratings.csv`) and movies data (`movies.csv`) while optimizing memory usage. It computes average ratings for each movie and merges them with the movie details.  

   - **User-Movie Matrix Creation**:  
     The system creates a **sparse user-movie matrix** where rows represent users, columns represent movies, and the values are the ratings given by users. Missing ratings are filled with zeros to maintain matrix consistency.  

   - **Similarity Calculation**:  
     The system calculates the **cosine similarity** between movie vectors using the sparse matrix. Cosine similarity measures how similar two movies are based on user ratings, which helps in identifying movies similar to the ones the user has watched.  

   - **Finding Top Recommendations**:  
     For each movie selected by the user, the system finds the **top 10 similar movies** by sorting the similarity scores. These movies are then ranked and displayed as recommendations.  

4. **Recommendation Display**:  
   The final recommendations are presented to the user in a clean, interactive format on the web interface, allowing users to explore new movies that match their taste.  


## Dataset

The system employs a small subset of the [MovieLens](https://grouplens.org/datasets/movielens/) dataset, which includes:

- **Ratings Data**: User ratings for various movies.
- **Movies Data**: Details about movies such as titles and genres.

Only a small part of the MovieLens dataset was selected for this project, rather than using the entire dataset, to optimize performance and focus on relevant movie recommendations.

## Visualization

Below are images showcasing the application in action:

**1. Home Page (Index)** - The starting point of the application.

![Home_Page](https://github.com/ManasiBhosale/MovieRecommendation/blob/bd46b07724eb088f796e58a1ffe65d5b29e11cb8/Images/IndexPage.png)

 <br />
 
**2. Recommendations by Year** - Suggested movies based on a selected year.

![Recommendation_By_Year](https://github.com/ManasiBhosale/MovieRecommendation/blob/bd46b07724eb088f796e58a1ffe65d5b29e11cb8/Images/YearBasedSearch.png)

 <br />
 
**3. Recommendations by Genre** - Suggested movies based on a selected genre.

![Recommendation_By_Genre](https://github.com/ManasiBhosale/MovieRecommendation/blob/bd46b07724eb088f796e58a1ffe65d5b29e11cb8/Images/GenreBasedSearch.png)

 <br />   
 
**4. Selection Page** - Interface for choosing movies the user has already watched.

![More_Recommend1](https://github.com/ManasiBhosale/MovieRecommendation/blob/bd46b07724eb088f796e58a1ffe65d5b29e11cb8/Images/more_recommend1.png)

<br />  

**5. Final Recommendations** - Movies recommended based on the user’s previous selections.

![More_Recommend2](https://github.com/ManasiBhosale/MovieRecommendation/blob/bd46b07724eb088f796e58a1ffe65d5b29e11cb8/Images/more_recommend2.png)


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

   - Choose movies based on **year** or **genre**.
   - Select movies you have already watched to improve recommendation accuracy.
   - Receive personalized movie suggestions based on similar users' ratings.

## Project Structure

- **`app.py`**: Main Flask application file.
- **`data/`**: Directory containing the dataset files.
- **`scripts/`**: Contains scripts for data processing and recommendation algorithms.
- **`templates/`**: HTML templates for the web interface.
- **`static/styles/`**: CSS stylesheets for the web interface.
- **`requirements.txt`**: List of Python dependencies.

## Acknowledgments

Special thanks to the [MovieLens](https://grouplens.org/datasets/movielens/) project for providing the dataset used in this system.

