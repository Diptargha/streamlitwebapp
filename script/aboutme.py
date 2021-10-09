import streamlit as st
import streamlit.components.v1 as stc

from script import about_me_template as template
from script import all_images as im


def _main():
    """includes all items in the aboutme page"""

    col1, col2 = st.columns([0.4, 0.6])
    with col1:
        st.image(im.image_author, width=400)
        stc.html(template.html_aboutme_template(), height=250)

    with col2:
        st.write('# About me')
        stc.html("""
                <div style='background-color:black;padding:2px 4px;border-radius:20px;opacity:1; height:200'>
                <h2 style='color:white;text-align:left;font-weight: normal;font-size: 24px;font-family: sans-serif'
                >  Hello! My name is Diptargha Chakravorty. I am a Power Systems consultant working in the area of 
                renewable energy and its impact on the electricity network. I created this app as a hobby 
                project. Now it serves as a useful plotting tool. Hope you find it useful as well! 
                </div>
                """, height=400)


def run():
    _main()
