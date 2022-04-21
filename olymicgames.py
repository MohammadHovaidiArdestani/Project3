import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import altair as alt
from vega_datasets import data
import seaborn as sns

@st.cache
def load_data():
    url="https://raw.githubusercontent.com/matzim95/ML-datasets/master/olympic.csv"
    data = pd.read_csv(url)
    return data

st.markdown("Streamlit_Olypmic")
df1 = load_data()
df  = pd.DataFrame(df1)
#st.write(df)

df_selected = df.loc[df["Medal"].notnull()]
df_group = df_selected.groupby("Team").count().reset_index()
df_filter = df_group.loc[df_group['Medal']  > 500]

st.dataframe(df_filter)

source= df_filter#pd.merge(df_filter, df_filter1, how="left", on="Team")

bars = alt.Chart(source).mark_bar().encode(
    x=alt.X('sum(Medal)', stack='zero'),
    y=alt.Y('Team'),
    color=alt.Color('Medal')
)


text = alt.Chart(source).mark_text(dx=-15, dy=3, color='white').encode(
    x=alt.X('sum(Medal):Q', stack='zero'),
    y=alt.Y('Team:N'),
    detail='Medal:N',
    text=alt.Text('sum(Medal):Q', format='.1f')
)

st.write(bars + text)

fig1 = sns.relplot(data=source, x="Medal", y="Team")

#fig1.set_yticks(range(len(filtered_data)-5))

# ax.xaxis.set_tick_params(rotation=30, labelsize=10)

st.pyplot(fig1)

#groupby("Team")


#df_group1 = df_selected.groupby(["Team","Medal"]).size().reset_index()
#df_filter1 = df_group1.set_index(["Team"])
#st.write(df_group1)
