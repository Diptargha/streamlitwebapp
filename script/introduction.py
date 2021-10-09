import streamlit as st
from PIL import Image
import urllib.request as request


def page_introduction():
    # Space so that 'About' box-text is lower
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")
    st.sidebar.write("")

    st.markdown("<h2 style='text-align: center; color: grey;'> Welcome To </h2>",
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> Data Explorer</h1>",
                unsafe_allow_html=True)

    st.info("""
            There are two main features: \n
            - Explore datasets
            - Fit distributions (coming up) \n
            $←$ To start playing with the app, select an option on the 
            left sidebar.
            """)

    image1 = "https://github.com/Diptargha/streamlitwebapp/blob/master/images/step%201.PNG?raw=true"
    image2 = "https://github.com/Diptargha/streamlitwebapp/blob/master/images/step%202.PNG?raw=true"
    image3 = "https://github.com/Diptargha/streamlitwebapp/blob/master/images/step%203.png?raw=true"
    image4 = "https://github.com/Diptargha/streamlitwebapp/blob/master/images/step%204.png?raw=true"
    image5 = "https://github.com/Diptargha/streamlitwebapp/blob/master/images/step%205.png?raw=true"

    def make_line():
        """ Line divider between images. """

        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                           unsafe_allow_html=True)

        return line

    # Images and brief explanations.
    # request.urlretrieve('https://github.com/Diptargha/streamlitwebapp/tree/master/images',
    #                     "test.png")
    # image = Image.open("C:\Users\chakravortyd\Documents\GitHub\streamlitwebapp\images\test.png")

    st.error('Explore datasets')
    feature1, feature2 = st.columns([0.6, 0.4])
    with feature1:
        st.image(image1, use_column_width=True)
    with feature2:
        st.warning('Select a csv file')
        st.info("""
                - Either select a file using the *Browse files* option
                - Or drag and drop a file over it
                - Use the provided sample csv file *Irish Dataset.csv * if you don't have one at hand
                """)

    make_line()

    feature3, feature4 = st.columns([0.6, 0.4])
    with feature3:
        st.image(image2, use_column_width=True)
    with feature4:
        st.warning('Data columns at a glance')
        st.info("""
                - Click on the expander to see data columns
                - Scroll on the side/bottom to see more rows and columns 
                """)
    make_line()

    feature5, feature6 = st.columns([0.6, 0.4])
    with feature5:
        st.image(image3, use_column_width=True)
    with feature6:
        st.warning('Feature selection')
        st.info("""
                - Option to select two features (data columns from the csv file)
                - If the dataset has categorical columns, two more feature selection is made available
                """)

    make_line()

    feature7, feature8 = st.columns([0.6, 0.4])
    with feature7:
        st.image(image4, use_column_width=True)
    with feature8:
        st.warning('Categorical feature')
        st.info("""
                - Set *categorical dataset* option to *Yes*
                - Select a categorical column from the list of features
                - option to select a fourth feature, this should be a column with numerical values
                """)

    make_line()

    return
