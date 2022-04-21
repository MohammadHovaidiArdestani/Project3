import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime, timedelta
import seaborn as sns
import altair as alt


min_date = datetime(2019, 1, 3)
max_date = datetime(2019, 8, 27)

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

#df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
#df['Date'] = df['Date'].apply(pd.Timestamp)
#df["Date"] = df["Date"].to.Timestamp
#print("*E*EE*EE**E*EE**")
#print(df["Date"])



start = st.sidebar.date_input("Select the start date", min_value = min_date, max_value = max_date, value = min_date)
start = pd.Timestamp(start)
days = st.sidebar.number_input("How many days?", 3)
#df['Date'] = df[df['Date'].between(start, start+timedelta(days=days))]
#date_ranges = df[(df["Date"] >= start) & (df["Date"] <= start + days)]
#date_ranges = df.loc[(df["Date"] >= "2019-03-01") & (df["Date"] <= "2019-03-03")]
##print("**********************")
##print(type(df["Date"].to_frame))


##st.write('This is a Rate.')
##df_selected = df[["Date", "Rate"]]
#df = data.rename(columns={'date':'index'}).set_index('Rate')
##st.line_chart(df_selected)


#select a starting date here
date_options = df['Date'].unique().tolist()
start_date = st.selectbox("Please select the starting date: ", date_options, 0)
# the_right_starting_date = df['Date']=start_date


#select an ending date here
end_date = st.selectbox("Please select the ending date: ", date_options, 0)
# the_right_ending_date = df['Date']=end_date

filtered_data =  df[(df['Date']>=start_date) & (df['Date']<=end_date)]
#df_selected = filtered_data[["Date", "Rate"]]

#fig1 = sns.relplot(data=filtered_data, x="Date")

#st.pyplot(fig1)
#st.line_chart(df_selected)

fig, ax = plt.subplots(figsize=(10, 10))
# Add x-axis and y-axis
ax.plot(filtered_data['Date'],
        filtered_data['Rate'],
        color='purple')


ax.set(xlabel="Date",
       ylabel="Rate",
       title="Convertion rate of VES and USD")
plt.setp(ax.get_xticklabels(), rotation=45)
ax.set_xticks(np.arange(0, len(filtered_data['Date'])+1, 5))
ax.set_yticks(np.arange(0, len(filtered_data['Rate'])+1, 5))
plt.show()
st.pyplot(fig)

df = filtered_data[["Date", "Rate"]]
#df = df.rename(columns={'Date':'index'}).set_index('index')
df = df.set_index('Date')
st.header("Convertion rate of VES and USD")
st.line_chart(df)


