import streamlit as st
import streamlit.components.v1 as stc
from streamlit_lottie import st_lottie

from script.ui_components import load_lottieurl
from script import all_images as im


def _main():
    """includes all items in the sweetviz page"""
    # temp = st.columns(1)
    temp = st.empty()
    with temp:
        st_lottie(load_lottieurl(im.image_comingsoon))


def run():
    _main()
