🎬 Movie Recommendation System

A Content-Based Movie Recommendation System built using Python and Machine Learning.
The system recommends movies similar to a selected movie by analyzing movie features such as cast, crew, genres, and keywords.

It uses cosine similarity to find the most similar movies and suggests the top 5 recommendations.

📌 Project Overview

With thousands of movies available on online platforms, it becomes difficult for users to find movies that match their interests.
This project solves this problem by recommending movies that are similar to the one selected by the user.

The system analyzes important movie features and generates recommendations based on similarity between movies.

⚙️ How the System Works

The workflow of the system is:

1️⃣ Dataset Collection
Movie dataset containing information like title, cast, crew, genres, and keywords is used.

2️⃣ Data Preprocessing
Relevant features are extracted from the dataset.

3️⃣ Feature Engineering
Features such as:

Cast
Crew
Genres
Keywords

are combined into a single column called tags.

4️⃣ Vectorization
The tags are converted into numerical vectors using Count Vectorizer.

5️⃣ Similarity Calculation
Cosine similarity is used to calculate similarity between movie vectors.

6️⃣ Recommendation Generation
When a movie is selected, the system finds the top 5 most similar movies and displays them with posters.

🧠 Algorithm Used

The recommendation system uses Content-Based Filtering.

Content-based filtering recommends items that are similar to the user's selected item based on features.

The similarity between movies is calculated using the Cosine Similarity formula.

🛠 Technologies Used
Python
Pandas
NumPy
Scikit-Learn
Streamlit
Pickle
TMDB API (for movie posters)
📂 Project Structure
Movie_Recommendation_System
│
├── app.py
├── movie_dict.pkl
├── similarity.pkl
├── requirements.txt
├── README.md
▶️ Running the Project
1️⃣ Clone the repository
git clone https://github.com/yourusername/movie-recommendation-system.git
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the Streamlit app
streamlit run app.py

The application will open in your browser.

🎥 Application Features

✔ Select a movie from the dropdown menu
✔ Get Top 5 similar movie recommendations
✔ Movie posters are displayed for better user experience
✔ Fast similarity search using precomputed similarity matrix

📊 Example Output

If the user selects a movie like Avatar, the system recommends similar movies based on content similarity.

Example recommendations may include:

Guardians of the Galaxy
John Carter
Star Trek
Jupiter Ascending
The Fifth Element
🚀 Future Improvements

Some possible improvements for this system:

Add collaborative filtering
Use deep learning recommendation models
Add user ratings
Improve UI design
Deploy the system online
