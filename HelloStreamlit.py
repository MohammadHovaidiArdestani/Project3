import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
import plotly.express as px
import pyodbc

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Project3 Team1 Visualization")
st.sidebar.image("lh.png")

#conn = pyodbc.connect(driver='{SQL Server Native Client 11.0}', host='rg-data-project.database.windows.net', database='rg-data-project-team1',
#                      user='sqladminuser', password='Admin123+')
#def init_connection():
#    return pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + st.secrets["server"] + ";DATABASE=" + st.secrets["database"] + ";UID="       
#        + st.secrets["username"]
#        + ";PWD="
#        + st.secrets["password"]
#    )

#conn = init_connection()
#chunk_test = pd.read_sql('SELECT * from CampaignAnalytics', conn)

@st.cache
def load_data(nrows):
    data = pd.read_csv('test.csv', nrows=nrows)
    return data

st.markdown("Campaign Analytics Data")

chunk_test = load_data(1000)


st.markdown("Campaign Analytics Data")
#chunk_test = load_data(500)

#st.subheader("import the first chunk")
st.write(chunk_test)

df  = pd.DataFrame(chunk_test)

sidebar = st.sidebar
Region_selector = sidebar.selectbox(
    "Select a Region",
    df.Region.unique()
)

country_selector = sidebar.selectbox(
    "Select a country",
    df.Country.unique()
)

product_selector = sidebar.selectbox(
    "Select a product",
    df.ProductCategory.unique()
)

df_selected = df.loc[(df["Region"] == Region_selector) & (df["Country"] == country_selector) & (df["ProductCategory"] == product_selector)]

show_data = sidebar.checkbox("Show Data")
if show_data:
    st.dataframe(df_selected)

values = st.sidebar.slider("Revenue range", float(df_selected["Revenue"].min()), float(df_selected["Revenue"].max()), (0.0, 100.0))
f = px.histogram(df.query(f"Revenue.between{values}"), x="Revenue", nbins=15, title  = "Revenue distribution")
f_corr = px.scatter(df.query(f"Revenue.between{values}"), x = "Revenue", y = "RevenueTarget" )
st.plotly_chart(f)
st.plotly_chart(f_corr)

st.subheader(f"The {product_selector} product of {country_selector} in {Region_selector} has the following Revenue per Campaign:")
df_selected.groupby(["CampaignName"]).sum().plot(kind = "pie", y = "Revenue", autopct='%.1f%%', shadow=True)
plt.legend(loc='lower left', prop={'size': 7})
plt.show()
st.pyplot()


st.subheader(f"The {product_selector} product of {country_selector} in {Region_selector} has the following RevenueTarget per Campaign:")
df_selected.groupby(["CampaignName"]).sum().plot(kind = "pie", y = "RevenueTarget", autopct='%.1f%%')
plt.legend(loc='lower left', prop={'size': 7})
plt.show()
st.pyplot()

st.bar_chart(df_selected.groupby(["CampaignName"]).sum("RevenueTarget"))

df_selected.plot.bar(x='CampaignName', y = ["Revenue","RevenueTarget"])
plt.legend(loc='upper right', prop={'size': 7})
plt.show()
st.pyplot()
