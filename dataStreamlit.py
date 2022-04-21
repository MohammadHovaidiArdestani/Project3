import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import io
@st.cache
def load_data():
    url="https://raw.githubusercontent.com/matzim95/ML-datasets/master/ves-usd.csv"
    #r = requests.get(url)
    #open('temp.csv', 'wb').write(r.content)
    #data = pd.read_csv('temp.csv')
    data = pd.read_csv(url)
    return data
st.markdown("Streamlit_Master")
df = load_data()
#st.write(data)
sidebar = st.sidebar
show_data = sidebar.checkbox("Show Data")
if show_data:
    st.dataframe(df)


df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')

date_options = df['Date'].unique().tolist()
date = st.selectbox("which date would you like to see?", date_options,0)




st.write('This is a Rate.')
df_selected = df["Rate"]
#df = data.rename(columns={'date':'index'}).set_index('Rate')
st.line_chart(df_selected)