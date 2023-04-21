import streamlit as st
import pandas as pd
import numpy as np


df1 = pd.read_csv("pub.csv")


st.markdown('<h1 style="color:green">UK MAP PUB Locations</h1>', unsafe_allow_html=True)


local = df1.local_authority.unique()
st.sidebar.markdown("Chosing the Area")
option = st.sidebar.selectbox('',local)


'You Selected : ' ,option



btn_clk = st.button('Search')
if btn_clk==True:
    res = df1[df1['local_authority']==option]
    res=res[['latitude','longitude']]
    st.success('It display\'s all the pubs in the area that are selected')
    st.map(res)
