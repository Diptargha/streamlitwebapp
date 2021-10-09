import streamlit as st
import streamlit.components.v1 as stc

from script import create_slideshow as slideshow
from script import all_images as im


def _main():
    """includes all items in the aboutme page"""
    # stc.html("<p style='color:red;'> Test </p>")
    html_test = """
    <div style='background-color:green;padding:10px;border-radius:10px;opacity:1'>
    <h2 style='color:white;test-align:left;font-weight: normal;font-size: 22px;font-family: sans-serif'
    > Steps to use the app </div>
    """

    html_test = slideshow.html_slideshow(im.image_step1, im.image_step2, im.image_step3)
    stc.html(html_test, height=800)


def run():
    _main()
