import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from PIL import Image

model = pickle.load(open("nba_model 2.pkl" , 'rb'))

st.title('Basket Ball Predictor')
st.sidebar.header('Players Date')
Players_image = Image.open("bskball.jpg")
st.image(Players_image, width=300)

def user_report():
    rating = st.sidebar.number_input('Players Rating', 0, 100)
    geo = st.sidebar.selectbox('Country', ('USA', 'Canada', 'Australia', 'Others'))
    if geo == 'USA':
        country = 0
    elif geo == 'Canada':
        country = 1
    elif geo == 'Australia':
        country = 2
    else:
        country = 3
    draft_year = st.sidebar.slider('Draft Year', 2000, 2050)
    draft_round = st.sidebar.slider('Draft round', 1, 20 )
    draft_peak = st.sidebar.slider('Draft Peak', 1, 50)
    Age = st.sidebar.number_input('Player Age', 0, 50)


    user_report_date = {
        'rating' : rating,
        'country' : country,
        'draft_year' : draft_year,
        'draft_round' : draft_round,
        'draft_peak' : draft_peak,
        'Age' : Age
    }
    report_data = pd.DataFrame(user_report_date, index=[0])
    return report_data
user_data = user_report()

st.subheader('Player data summary')
st.write(user_data)

salary = model.predict(user_data)

st.subheader('Player salary')
st.subheader('$' + str(np.round(salary[0])))

