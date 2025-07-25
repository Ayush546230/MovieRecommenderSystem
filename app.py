import pandas as pd
import streamlit as st
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movies_list:
        movie_id=i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dictionary = pickle.load(open('movies_dict.pkl', 'rb'))
movies=pd.DataFrame(movies_dictionary)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

option = st.selectbox(
    "Select your favourite movie",
    movies['title'].values,
    index=None,
    placeholder="Select the movie.....",)

if st.button("Recommend"):
    recommendations=recommend(option)
    for j in recommendations:
        st.write(j)