"""
A simple streamlit app to load csv files and plot the data for each column
"""

import streamlit as st
from streamlit_lottie import st_lottie
from script import csv_file_explorer
from script.ui_components import load_lottieurl
from script.introduction import page_introduction
from script import all_images as im
from script import create_sweetviz_report
from script import aboutme

st.set_page_config(layout="wide", page_title='Data Explorer')

logo, name = st.sidebar.columns([0.6, 0.4])
with logo:
    st_lottie(load_lottieurl(im.image_datacharts2))
with name:
    st.markdown("<h1 style='text-align: left; color: grey; font-size: 32px'> \
                Data Explorer </h1>", unsafe_allow_html=True)

st.sidebar.write(" ")


def main():
    """calling individual pages on the website"""

    pages = {
        "Home": page_introduction,
        "Explore through charts": csv_file_explorer.run,
        "Explore through Sweetviz": create_sweetviz_report.run,
        "About the author": aboutme.run,
    }

    st.sidebar.title("Page options")

    # Radio buttons to select desired option
    page = st.sidebar.radio("Select:", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page]()

    # Write About
    st.sidebar.header("About")
    st.sidebar.warning(
        """
            Data Explorer app is created and maintained by 
            **Diptargha Chakravorty**. This is a very simple app 
            developed as an example for beginners. If you like this app please star its
            [**GitHub**](https://github.com/Diptargha/streamlitwebapp)
            repo, share it and feel free to open an issue if you find a bug 
            or if you want some additional features.
            """
    )


if __name__ == "__main__":
    main()
