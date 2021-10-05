import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_title="Art",
    page_icon="🎭",
    layout="centered",
    initial_sidebar_state="expanded",
)

app_state = st.experimental_get_query_params()
if 'region' in app_state.keys():
    region = app_state['region'][0]
else:
    region = 'dutch'

if 'artist' in app_state.keys():
    artist = app_state['artist'][0]
else:
    artist = 'franshals'

region_artist = {'dutch':["Frans Hals","Rembrandt Van Rijn","Johannes Vermeer"],
                 'france':["Nicolas Poussin", "Jules Hardouin-Mansart", "François Girardon"]}

def yeardata(artist):
    ans = []
    for i in range(len(os.listdir(artist))-2):
        f = open(f"{artist}/{i+1}/info.txt")
        ans.append(f.readline().strip())
        f.close()
    return ans, len(os.listdir(artist))-2

st.sidebar.markdown("<h1>Region:</h1>", unsafe_allow_html=True)
region_sb = st.sidebar.selectbox('',('Dutch', 'France'))
region_sb = region_sb.lower().replace(" ","")
if region_sb!=region:
    st.experimental_set_query_params(**{"artist": artist, 'region':region_sb})
region = region_sb

st.sidebar.markdown(f"<h1>Artist from {region.title()}:</h1>", unsafe_allow_html=True)
artist_name = st.sidebar.radio("",region_artist[region])
artist_sb = artist_name.lower().replace(" ","")
if artist_sb!=artist:
    st.experimental_set_query_params(**{"artist": artist_sb, 'region':region})
artist = artist_sb
yearlst, n_art = yeardata(artist)

if n_art>1 and artist!='juleshardouin-mansart':
    year = st.select_slider("Year",yearlst)
elif n_art==1 and artist!='juleshardouin-mansart':
    year = yearlst[0]
elif artist=='juleshardouin-mansart':
    year=None

artist_expander = st.expander(label='Artist Info',expanded=1)
with artist_expander:
    c1, c2 = st.columns((2,1))
    dp = Image.open(f'{artist}/dp.jpg')
    c1.image(dp,use_column_width=1)
    f = open(f"{artist}/info.txt")
    all_data = f.readlines()
    for info in all_data:
        c2.markdown(info.strip(), unsafe_allow_html=True)
    f.close()

art_expander = st.expander(label='Art')
with art_expander:
    if artist!='juleshardouin-mansart':
        f = open(f"{artist}/{yearlst.index(year)+1}/info.txt")
        f.readline()
        title = f.readline().strip()
        f.close()
        st.markdown(f"<p style='font-size:20px'><b><center>{title}</center></b></p>", unsafe_allow_html=True)
        art = Image.open(f'{artist}/{yearlst.index(year)+1}/art.jpg')
        st.image(art,use_column_width='auto')
    else:
        st.write("check out this [link](https://www.360cities.net/image/dsc7721-panorama)")