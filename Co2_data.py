import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import requests
import io

import seaborn as sns
import matplotlib.ticker as ticker

from matplotlib.dates import (YEARLY, DateFormatter,
                              rrulewrapper, RRuleLocator, drange)


@st.cache
def load_data():
    url="https://raw.githubusercontent.com/matzim95/ML-datasets/master/co2.csv"
    data = pd.read_csv(url)
    return data

st.markdown("Streamlit_Co2")
df1 = load_data()
df  = pd.DataFrame(df1)
st.write(df)    
 
#Checking the data
# print(df.head())

#checking the datatypes
# print(df.dtypes['Date'])
# print(df.dtypes['Decimal Date'])
# print(df.dtypes['Average'])
# print(df.dtypes['Interpolated'])
# print(df.dtypes['Trend'])
# print(df.dtypes['Number of Days'])

#here we will filter the data - Think about odd values that could be mistakes and how we can filter them out

st.subheader(f"Scatter plot filter option based on a time period")

#select a starting date here
date_options = df['Date'].unique().tolist()
start_date = st.selectbox("Please select the starting date: ", date_options, 0)
# the_right_starting_date = df['Date']=start_date


#select an ending date here
end_date = st.selectbox("Please select the ending date: ", date_options, 0)
# the_right_ending_date = df['Date']=end_date

filtered_data =  df[(df['Date']>=start_date) & (df['Date']<=end_date) & (df['Average']>0)]

fig1 = sns.relplot(data=filtered_data, x="Date", y="Average")

#fig1.set_yticks(range(len(filtered_data)-5))

# ax.xaxis.set_tick_params(rotation=30, labelsize=10)

st.pyplot(fig1)