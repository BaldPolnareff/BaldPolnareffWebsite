import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image 
import glob 
import base64
from apps import curriculum_vitae
from apps import Procedural_artwork
from apps import blender_artwork
from apps import contact
from utils import *

st.set_page_config(page_title="Bald Polnareff", page_icon="🗿", layout="centered")

#st.image("logo.svg")
components.html(render_svg("logo.svg", height=None, width=None))


st.divider()

# A list of all apps in a dictionary; format: {"app_name": "app_icon"}
apps = [
    {"func": curriculum_vitae.app,   "title": "CV",                 "icon": "file-richtext-fill"},
    {"func": blender_artwork.app,    "title": "3D Artwork",         "icon": "box-fill"},
    {"func": Procedural_artwork.app, "title": "Procedural Artwork", "icon": "palette2"},
    {"func": contact.app,            "title": "Contact me",         "icon": "person-lines-fill"},
]
    
params = st.experimental_get_query_params()
    
# A list of all app titles
titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]

# A list of all app icons
icons = [app["icon"] for app in apps]

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

# using a sidebar to select the app
with st.sidebar:
    selected = option_menu(
        "About me", 
        options=titles,
        default_index=default_index,
        icons=icons,
        menu_icon="person-bounding-box",
    )
    

# Display the selected app

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break



