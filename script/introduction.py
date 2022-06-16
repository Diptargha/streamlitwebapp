import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as stc
from PIL import Image
import urllib.request as request
from script.ui_components import load_lottieurl
from script import add_html_css
from script import all_images as im


def page_introduction():
    """includes all items in the home page"""
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    # st.markdown("<h2 style='text-align: center; color: grey;'> Welcome To </h2>",
    #             unsafe_allow_html=True)
    stc.html(add_html_css.html_image(), height=200)

    # st.markdown("<h1 style='text-align: center;'> Data Explorer</h1>",
    #             unsafe_allow_html=True)

    col1, col2 = st.columns([0.45, 0.55])
    with col2:
        st.info("""
                There are two main features of this app: \n
                - Explore a dataset through different charts
                - Use Pandas Profiling report to get a deeper insight into the data \n
                Steps to use the app are explained below. Currently, the app supports
                *.txt* and *.csv* formats for the dataset. \n
                Please feel free to use the sample file if you don't have one to hand
                to explore the features.\n
                
                $←$ To start playing with the app, select an option on the 
                left sidebar.
                """)

    with col1:
        st_lottie(load_lottieurl(im.image_datacharts1), height=380)

    def make_line():
        """ Line divider between images. """

        line = st.markdown('<hr style="border:1px solid green"> </hr>',
                           unsafe_allow_html=True)

        return line

    # Images and brief explanations.
    # request.urlretrieve('https://github.com/Diptargha/streamlitwebapp/tree/master/images',
    #                     "test.png")
    # image = Image.open("C:\Users\chakravortyd\Documents\GitHub\streamlitwebapp\images\test.png")

    st.markdown("<h2 style='text-align: left; color: green;'>Steps to use the app</h2>", unsafe_allow_html=True)
    st.success(" ")
    # st.info("## Steps to use the app")

    feature1, feature2 = st.columns([0.6, 0.4])
    with feature1:
        st.image(im.image_step1, use_column_width=True)
    with feature2:
        st.warning('Select a csv file')
        st.info("""
                - Either select a file using the *Browse files* option
                - Or drag and drop a file over it
                - Use the provided sample csv file *Irish Dataset.csv * if you don't have one to hand
                """)

    make_line()

    feature3, feature4 = st.columns([0.6, 0.4])
    with feature3:
        st.image(im.image_step2, use_column_width=True)
    with feature4:
        st.warning('Data columns at a glance')
        st.info("""
                - Click on the expander to see data columns
                - Scroll on the side/bottom to see more rows and columns 
                """)
    make_line()

    feature5, feature6 = st.columns([0.6, 0.4])
    with feature5:
        st.image(im.image_step3, use_column_width=True)
    with feature6:
        st.warning('Feature selection')
        st.info("""
                - Option to select two features (data columns from the csv file)
                - If the dataset has categorical columns, two more feature selection is made available
                """)

    make_line()

    feature7, feature8 = st.columns([0.6, 0.4])
    with feature7:
        st.image(im.image_step4, use_column_width=True)
    with feature8:
        st.warning('Categorical feature')
        st.info("""
                - Set *categorical dataset* option to *Yes*
                - Select a categorical column from the list of features
                - option to select a fourth feature, this should be a column with numerical values
                """)

    make_line()

    feature9, feature10 = st.columns([0.6, 0.4])
    with feature9:
        st.image(im.image_step5, use_column_width=True)
    with feature10:
        st.warning('Chart selection')
        st.info("""
                - Select a chart type from the drop-down menu
                - Charts are created using plotly and seaborn
                """)

    make_line()

    # html_test = slideshow.html_slideshow(im.image_step1, im.image_step2, im.image_step3)
    # stc.html(html_test, height=800)

    return
