import streamlit as st
import streamlit.components.v1 as stc
from streamlit_lottie import st_lottie

from script.ui_components import load_lottieurl
from script import all_images as im

def _main():
    """includes all items in the sweetviz page"""

    st.write("almost there...")
    st_lottie(load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_m6cuL6.json"))


def run():
    _main()
