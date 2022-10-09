'''# Streamlit
 Python to -> Frontend

to run do not press play button, but instead , in the terminal, type:
cd app_one
streamlit run app.py

'''


import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px


st.set_page_config(
    page_title="App One",
    page_icon="📑",
    layout="wide"
)

st.title("Streamlit data one")
st.subheader("very easy data analytics in python")


# Caching data 
@st.cache
def load_data():
    return pd.read_csv("cps_85_wages.csv")



# not the best way to load data 
# because data will load everytime we start/refresh
# using cache data technique
df=pd.read_csv("cps_85_wages.csv")
df=load_data()
st.dataframe(df,use_container_width=True)
st.bar_chart(df,x="WAGE",y="EDUCATION",use_container_width=True)




st.sidebar.header("Select Option")
if st.sidebar.checkbox("Show Pivot table Summary"):
    st.subheader("Pivot table summary")
    c1,c2 = st.columns(2)
    categorical_cols=df.select_dtypes(exclude=np.number).columns
    numeric_cols = df.select_dtypes(include=np.number).columns
    index_col = c1.selectbox("Pivot Index",options = categorical_cols)
    values_col = c1.multiselect("Pivot values", options = numeric_cols)
    func=c1.selectbox("Pivot Function",options=["mean","sum","count","min","max","std"])
    pivot_df=df.pivot_table(index=index_col,values=values_col,aggfunc=func)
    c2.dataframe(pivot_df,use_container_width=True)
    for col in values_col:
        fig = px.pie(pivot_df,values=col,names=pivot_df.index)
        st.plotly_chart(fig)


    




