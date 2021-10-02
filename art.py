import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="SPI:Calc",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="expanded",
)

def yeardata(artist):
    ans = []
    for i in range(len(os.listdir(artist))-2):
        f = open(f"{artist}/{i+1}/info.txt")
        ans.append(f.readline().strip())
        f.close()
    return ans, len(os.listdir(artist))-2
st.sidebar.markdown("<h1>Artist:</h1>", unsafe_allow_html=True)
artist_name = st.sidebar.radio("",("Frans Hals","Rembrandt Van Rijn","Nicolas Poussin"))
artist = artist_name.lower().replace(" ","")
yearlst, n_art = yeardata(artist)
year = st.select_slider("Year",yearlst)

artist_expander = st.expander(label='Artist Info',expanded=1)
with artist_expander:
    c1, c2 = st.columns((2,1))
    dp = Image.open(f'{artist}/dp.jpg')
    c1.image(dp,use_column_width=1)
    c2.markdown(f"<b><u>{artist_name.title()}</u></b>", unsafe_allow_html=True)
    f = open(f"{artist}/info.txt")
    c2.markdown(f.readline().strip(), unsafe_allow_html=True)
    c2.markdown(f.readline().strip(), unsafe_allow_html=True)
    f.close()

art_expander = st.expander(label='Art')
with art_expander:
    f = open(f"{artist}/{yearlst.index(year)+1}/info.txt")
    f.readline()
    title = f.readline().strip()
    f.close()
    st.markdown(f"<p style='font-size:20px'><b><center>{title}</center></b></p>", unsafe_allow_html=True)
    art = Image.open(f'{artist}/{yearlst.index(year)+1}/art.jpg')
    st.image(art,use_column_width='auto')