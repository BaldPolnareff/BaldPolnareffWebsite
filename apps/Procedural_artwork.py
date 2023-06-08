import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image 
import glob 
from utils import *

def app():
    st.header('My Procedural Artwork')
    st.write("Procedural Artwork is a form of generative art, where the artist creates an algorithm that generates the artwork. \n"
             "These shaders are written in GLSL, a C-like language that is used to write shaders for OpenGL and WebGL. \n")
    components.iframe("https://www.shadertoy.com/embed/dtcXWX?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/mtdXDs?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/DlGXzz?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/dtyXRR?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/dlySzR?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/ctGSRw?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/dtKSDR?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
    components.iframe("https://www.shadertoy.com/embed/DtGSD1?gui=false&t=10&paused=false&muted=false", height=300, scrolling=True)
