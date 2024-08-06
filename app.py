import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(music_title):
    url = 'https://saavn.dev/api/search/songs'
    query = {"query" : music_title}
    res = requests.get(url, params=query)
    data = res.json()
    return data['data']['results'][0]['image'][1]['url']


def recommend(musics):
    musicIndex = music[music['Song-Name'] == musics].index[0]
    distances = similarity[musicIndex]
    musicList = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommendedMusic = []
    recommendedMusicPoster = []
    for i in musicList:
        musicTitle = music.iloc[i[0]]['Song-Name']
        recommendedMusic.append(music.iloc[i[0]]['Song-Name'])
        recommendedMusicPoster.append(fetch_poster(musicTitle))
    return recommendedMusic, recommendedMusicPoster

with open(r'C:\Users\amay\Desktop\ML\Recommendation-Sys\musicrec.pkl', 'rb') as file:
    # musicDict = pd.read_pickle(file)
    music = pd.read_pickle(file)
with open(r'C:\Users\amay\Desktop\ML\Recommendation-Sys\similarities.pkl', 'rb') as file:
    similarity = pd.read_pickle(file)
st.title('Music Recommendation System')

selectedMusicNames = st.selectbox('Select a music you like', music['Song-Name'].values)

if st.button('Recommend'):
    names, posters = recommend(selectedMusicNames)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])