import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Nearest Pub"
)

df1 = pd.read_csv("new_pubs.csv")

st.markdown('<h1 style="color:green">Nearest five Pubs based on user enter Latitude and longitude</h1>', unsafe_allow_html=True)

lat = st.sidebar.number_input('The latitude of place')
lon = st.sidebar.number_input('The longitude of place')
button = st.button("Search")
df_new = df1[['latitude', 'longitude']]
new_points = np.array([lat, lon])

# Calculate distance between new_points and all points in df_new using Euclidean distance 
distances = np.sqrt(np.sum((new_points - df_new)**2, axis = 1))


# sort the array using arg partition and keep only 5 elements
n = 5
min_indices = np.argpartition(distances,n-1)[:n]
if button:
    st.map(df1.iloc[min_indices])
    st.text("The location corresponding to below nearest distances : ")
    st.dataframe(df1.iloc[min_indices])
    
    







