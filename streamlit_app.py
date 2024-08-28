import streamlit as st
import pickle
import pandas as pd

# Load the movies dictionary and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Define the recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movies = [movies.iloc[i[0]].title for i in movies_list]
    return recommend_movies

# Apply custom CSS for a better look
st.markdown("""
    <style>
    .reportview-container {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
        color: #ffffff;
    }
    .sidebar .sidebar-content {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        font-size: 18px;
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
    }
    h1 {
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.6);
    }
    .recommended-movies {
        color: #f5f5f5;
        font-size: 20px;
        font-weight: bold;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI
st.title('🎬 Movie Recommender System')

selected_movie_name = st.selectbox(
    'Type the movie of your choice:',
    movies['title'].values
)

if st.button('Recommend'):
    recommended_movie_names = recommend(selected_movie_name)
    st.write("### Here are some movies you might like:")
    for name in recommended_movie_names:
        st.markdown(f"<div class='recommended-movies'>- {name}</div>", unsafe_allow_html=True)
