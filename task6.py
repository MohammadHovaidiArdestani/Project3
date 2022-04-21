from itertools import groupby
import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import io
import altair as alt

import seaborn as sns

st.subheader(f"The Olympic Dataset")
@st.cache
def load_data():
    url="https://raw.githubusercontent.com/matzim95/ML-datasets/master/olympic.csv"
    data = pd.read_csv(url)
    return data

# st.markdown("Streamlit_Olypmic")
df1 = load_data()
df  = pd.DataFrame(df1)
st.write(df)


st.subheader(f"Boxplot for a sport based on Age, Height, Weight")

#Select the sport
sport_options = df['Sport'].unique().tolist()
selected_sport = st.selectbox("Please select the sport: ", sport_options, 0)

filtered_data = df[df['Sport']==selected_sport]

st.write(filtered_data)


# fig = sns.boxplot(data = filtered_data, y=df["Age"], x=df["Name"])
# plt.show()
# st.pyplot(fig)

# sns.boxplot(x=df["Name"], y=df["Age"], data = filtered_data)


#violin plot 
# plt.figure(figsize=(8, 6))
# fig1 = sns.violinplot(data = filtered_data, x = 'Age', y = 'Name')
# fig1.figure


boxfig = sns.boxplot(x=filtered_data['Age'], y=filtered_data['City'], data=filtered_data, orient="h",)
boxfig.figure

viofig = sns.violinplot(x=filtered_data['Height'],  y=filtered_data['City'], data=filtered_data, orient="h")
viofig.figure

swarmfig = sns.swarmplot(x=filtered_data['Weight'], y=filtered_data['City'], data=filtered_data, orient="h")
swarmfig.figure