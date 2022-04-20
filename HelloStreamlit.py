import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Project3 Team1 Visualization")
st.sidebar.image("lh.png")

@st.cache
def load_data(nrows):
    data = pd.read_csv('test.csv', nrows=nrows)
    return data

st.markdown("Campaign Analytics Data")
chunk_test = load_data(500)

#st.subheader("import the first chunk")
#st.subheader("import the first chunk")
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

st.subheader(f"The {product_selector} product of {country_selector} in {Region_selector} has the following Revenue per Campaign:")

show_data = sidebar.checkbox("Show Data")
if show_data:
    st.dataframe(df_selected)

df_selected.groupby(["CampaignName"]).sum().plot(kind = "pie", y = "Revenue", autopct='%.1f%%')
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
