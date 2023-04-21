import streamlit as st
import pandas as pd
from PIL import Image
from matplotlib import image
import numpy as np
import os

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.title(":green[Welcome to Homepage! 👋]")
st.snow()



st.title(":red[Innomatics Research Labs]")

#Adding Image
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
dir_of_interest = os.path.join(FILE_DIR, "resources")
IMAGE_PATH = os.path.join(dir_of_interest, "image")
IMAGE_PATH1 = os.path.join(IMAGE_PATH, "pub.jpg")

img = image.imread(IMAGE_PATH1)
st.image(img)

title = '<h1 style="font-family:sans-serif; color:Green; font-weight:bold">PUB\'s IN UNITED KINGDOM</h1>'
st.markdown(title, unsafe_allow_html=True)


st.subheader("Information about the pubs")



df1 = pd.read_csv("data\pub.csv")




# Using object notation
information = st.sidebar.selectbox(
    ":red[Statistical Data]",
    ('Number of Pub\'s','Data_shape','Head', 'Tail', 'Unique Area\'s', 'Null values', 'Describe'))

if information=='Number of Pub\'s':
    st.markdown(f'**{df1.shape[0]}**  Pubs  in  **UK**')

elif information == 'Data_shape':
    st.text('Number of rows: {}'.format(df1.shape[0]))
    st.text('Number of columns: {}'.format(df1.shape[1]))

elif information == 'Head':
    st.dataframe(df1.head())

elif information == 'Tail':
    st.dataframe(df1.tail())

elif information=='Unique Area\'s':
    st.markdown(f'Total number of unique locations where pubs are present in UK is **{len(df1.local_authority.unique())}** ')

elif information == 'Null values':
    st.markdown('**We can see that there are number of null values in the data**')
    st.table(df1.isna().sum())

elif information == 'Describe':
    st.table(df1.describe())


btn_click = st.button("Click me to Know Who I am")

if btn_click == True:
    st.subheader("You clicked me :cry:")
    st.balloons()
    st.title("I am :red[Bharathkumar M S]")
    st.title("I am a  :violet[ Data Science Enthusiast]")
    st.write("## Connect me on Linkedin [link](https://www.linkedin.com/in/bharathkumar-m-s-1736221b0/)")


