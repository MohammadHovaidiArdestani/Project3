import streamlit as st
import pandas as pd
import numpy as np
import plotly.figure_factory as ff
import matplotlib.pyplot as plt

st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Project3 Team1 Visualization")


@st.cache
def load_data(nrows):
    data = pd.read_csv('test.csv', nrows=nrows)
    return data

st.markdown("Campaign Analytics Data")
chunk_test = load_data(500)

#st.subheader("import the first chunk")
st.write(chunk_test)
#Bar Chart
#st.bar_chart(chunk_test["Revenue"])


#histogram
#df_hist = pd.DataFrame(chunk_test[:200], columns = ["Revenue","RevenueTarget"])
#df_hist.hist()
#plt.show()
#st.pyplot()

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
st.markdown(f"# you have selected {country_selector} in {Region_selector}")

df_selected = df.loc[(df["Region"] == Region_selector) & (df["Country"] == country_selector)]



show_data = sidebar.checkbox("Show Data")
if show_data:
    st.dataframe(df_selected)

#df_hist = pd.DataFrame(df_selected, columns = ["CampaignName","RevenueTarget"])
#df_hist.plot( x = "CampaignName" , y = "RevenueTarget", kind = "scatter")
#df_pie = pd.DataFrame(df_selected, columns = ["CampaignName"])
df_selected.groupby(["CampaignName"]).sum().plot(kind = "pie", y = "RevenueTarget", title = "RevenueTarget by campaign name")
plt.legend(loc = 0)
plt.show()
st.pyplot()

#revenue_target = df.groupby(pd.Grouper(key="Country", freq="1D")).aggregate(RevenueTarget=("Revenue", "sum")).reset_index()
#fig = revenue_target.iplot(kind="line", asFigure=True, 
                        #x="Country", y="RevenueTarget")
#st.plotly_chart(fig)