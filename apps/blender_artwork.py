import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image 
import glob 
from utils import *

def app():
    display_images_grid("./Images/*.jpg")
