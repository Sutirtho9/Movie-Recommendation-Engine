import streamlit as st
import pickle
import pandas as pd
import requests
movies_list= pickle.load(open('movies.pkl','rb'))
movies=pd.DataFrame(movies_list)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

st.title('Movie Recommender System')

similarity=pickle.load(open('similarity.pkl','rb'))

def recommender(movie):
    movie_index=movies[movies['title']== movie].index[0]
    distances= similarity[movie_index]
    movies_list=sorted(list(enumerate(distances)), reverse=True,key = lambda x: x[1])[1:11]
    
    recommended_movies=[]
    recommended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id

        recommended_movies.append(movies.iloc[i[0]].title)

        #fetch from API
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters



selected_movie=st.selectbox('Select Movie to get recommendations',movies['title'].values)

st.markdown("""
    <style>
    body {
        background-color: #141414;
        color: white;
    }
    .movie-card {
        background-color: #1f1f1f;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: transform 0.2s ease-in-out;
        height: 250px; /* Fixed height for consistency */
        overflow: hidden;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }
    .movie-card:hover {
        transform: scale(1.05);
    }
    .movie-title {
        font-size: 14px;
        color: white;
        text-align:center;
        margin-top: 10px;
        font-weight: bold;
        overflow: hidden;
    }
    .movie-row {
        margin-top: 30px; /* Add space between rows */
    }
    </style>
""", unsafe_allow_html=True)


if st.button('Recommend'):
    names, posters = recommender(selected_movie)

    for row in range(2):
        if row > 0:
            st.markdown('<div class="movie-row"></div>', unsafe_allow_html=True)
        
        cols = st.columns(5)
        for i in range(5):
            idx = row * 5 + i
            with cols[i]:
                st.markdown(f"""
                    <div class="movie-card">
                        <img src="{posters[idx]}" width="100%" style="border-radius:5px;" />
                        <p class="movie-title">{names[idx]}</p>
                    </div>
                """, unsafe_allow_html=True)

    
