import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
from PIL import Image 
import glob 
from utils import *

def app():
    st.header("Contact me")
    st.subheader("[Email](mailto:detranegiorgio@gmail.com) \n")
    st.subheader("[LinkedIn](https://www.linkedin.com/in/giorgiodetrane/) \n")
    st.subheader("[GitHub](https://www.github.com/BaldPolnareff) \n")
    # More info about me
    st.header("Who am I?")
    st.info(
        """
        I am an Aerospace Engineer with a passion for programming, data science, machine learning and 3D art.

        I am currently looking for a job in the field of data science, machine learning or software development, or 
        as a technical manager in those fields.
        """
    )

    st.header("About this website")
    st.info(
        """
        You can find the source code for this streamlit template on my [GitHub repo](https://www.github.com/BaldPolnareff/BaldPolnareffWebsite).
        
        Streamlit is an open-source app framweork typically used for data science dashboards and machine learning web applications, 
        but I wanted to showcase that it can be a flexible tool for creating a personal website, if you already know 
        Python and some basic Markdown and HTML.

        The code is distributed under the GPL-v3 license, so feel free to fork it and use it for your own website!
        """
    )



