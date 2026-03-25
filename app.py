import streamlit as st
import pickle
import pandas as pd
import requests
import time

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:60px;
    font-weight:700;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
}

.movie-card{
    padding:10px;
    border-radius:12px;
    background-color:#111;
    text-align:center;
    transition: transform 0.3s;
}

.movie-card:hover{
    transform: scale(1.05);
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
}
</style>
""", unsafe_allow_html=True)


# ---------- LOAD DATA ----------
@st.cache_data
def load_data():
    movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    return movies, similarity


movies, similarity = load_data()


# ---------- FETCH POSTER WITH CACHING ----------
@st.cache_data(ttl=3600)  # Cache for 1 hour
def fetch_poster(movie_id):
    # Try multiple poster services if one fails
    poster_urls = [
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY_1&language=en-US",
        f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY_2&language=en-US"
        # Backup API key
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    }

    for url in poster_urls:
        try:
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                data = response.json()
                poster_path = data.get("poster_path")

                if poster_path:
                    return "https://image.tmdb.org/t/p/w500/" + poster_path
                else:
                    # Return placeholder with movie title
                    movie_title = movies[movies['movie_id'] == movie_id].iloc[0]['title']
                    return f"https://via.placeholder.com/500x750?text={movie_title.replace(' ', '+')}"

            elif response.status_code == 429:  # Rate limited
                time.sleep(1)  # Wait and try next
                continue

        except:
            continue

    # If all APIs fail, return placeholder
    movie_title = movies[movies['movie_id'] == movie_id].iloc[0]['title']
    return f"https://via.placeholder.com/500x750?text={movie_title.replace(' ', '+')}"


# ---------- RECOMMEND FUNCTION ----------
def recommend(movie):
    try:
        movie_index = movies[movies['title'] == movie].index[0]
        distances = similarity[movie_index]

        movies_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )[1:6]

        recommended_movies = []
        recommended_posters = []

        for i in movies_list:
            movie_id = movies.iloc[i[0]].movie_id
            movie_title = movies.iloc[i[0]].title

            recommended_movies.append(movie_title)

            # Fetch poster with retry logic
            poster = fetch_poster(movie_id)
            recommended_posters.append(poster)

        return recommended_movies, recommended_posters

    except Exception as e:
        st.error(f"Error finding recommendations: {str(e)}")
        return [], []


# ---------- HEADER ----------
st.markdown("<div class='main-title'>🎬 Movie Recommendation System</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Find movies similar to your favorites</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------- MOVIE SELECT ----------
selected_movie_name = st.selectbox(
    "🔎 Search for a movie",
    movies['title'].values
)

# ---------- BUTTON ----------
if st.button("✨ Recommend"):

    names, posters = recommend(selected_movie_name)

    if names:
        st.markdown("## 🍿 Recommended For You")

        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.image(posters[i], use_container_width=True)
                st.markdown(f"<div class='movie-card'><b>{names[i]}</b></div>", unsafe_allow_html=True)
    else:
        st.warning("No recommendations found. Please try another movie.")
# ---------- FOOTER ----------
st.markdown("""
<div class='footer'>
Made with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
