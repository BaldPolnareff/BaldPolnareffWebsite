import streamlit as st 
from streamlit_option_menu import option_menu
import streamlit.components.v1 as components
import base64
from PIL import Image 
import glob 

def display_images_grid(image_path):
    """Display a grid of images
        Args: image_path (str): path to the image directory, in the form of "path/to/images/*.jpg"
    """
    image_paths = glob.glob(image_path)  # Update the path to your image directory
    image_paths.sort()  # Sort the images by name

    # Create a list of PIL Image objects
    images = [Image.open(path) for path in image_paths]

    # Evaluate the total number of images
    N_IMAGES = len(images)

    st.header('My Blender 3D Artwork')
    st.write("Pick a number of columns for a grid layout, then click on the expand button to see the images in full size. \n"
             "These images are 4K renders, give Streamlit a few seconds to load them. \n")
    with st.sidebar:
        st.subheader("Number of columns")
        n_cols = int(st.number_input("Enter a number", min_value=1, max_value=5, value=3, step=1))

    n_rows = int(1 + N_IMAGES // n_cols)
    rows = [st.container() for i in range(n_rows)]
    cols = [column for row in rows for column in row.columns(n_cols)]

    for col, image in zip(cols, images):
        with col:
            st.image(image, use_column_width=True)

#def render_svg(svg_file):
#
#    with open(svg_file, "r") as f:
#        lines = f.readlines()
#        svg = "".join(lines)
#
#        """Renders the given svg string."""
#        b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
#        html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
#        return html

def render_svg(svg_file, width=None, height=None):
    with open(svg_file, "r") as f:
        svg = f.read()

        # Set width and height attributes of the SVG
        if width and height:
            svg = svg.replace("<svg", f'<svg width="{width}" height="{height}"')

        # Add CSS to make the SVG responsive
        svg = svg.replace(f"<svg", '<svg style="max-width: 100%; height: auto;"')

        # Encode SVG as base64
        #b64 = base64.b64encode(svg.encode("utf-8")).decode("utf-8")
        #html = f'<img src="data:image/svg+xml;base64,{b64}"/>'
        return svg
