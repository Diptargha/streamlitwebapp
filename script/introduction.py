import streamlit as st


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

    st.markdown("<h2 style='text-align: center;'> Welcome To </h2>",
                unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center;'> Data Explorer</h1>",
                unsafe_allow_html=True)

    st.info("""
            There are two main features: \n
            - Explore datasets
            - Fit distributions (coming up) 
            $←$ To start playing with the app, select an option on the 
            left sidebar.
            """)

    image1 = "https://raw.githubusercontent.com/rdzudzar/DistributionAnalyser/main/images/Dist1.png?token" \
             "=AIAWV2ZQOGWADUFWZM3ZWBLAN3CD6 "
    image2 = "https://raw.githubusercontent.com/rdzudzar/DistributionAnalyser/main/images/Dist1.png?token" \
             "=AIAWV2ZQOGWADUFWZM3ZWBLAN3CD6 "
    image3 = "https://raw.githubusercontent.com/rdzudzar/DistributionAnalyser/main/images/Dist1.png?token" \
             "=AIAWV2ZQOGWADUFWZM3ZWBLAN3CD6 "

    def make_line():
        """ Line divider between images. """

        line = st.markdown('<hr style="border:1px solid gray"> </hr>',
                           unsafe_allow_html=True)

        return line

        # Images and brief explanations.

    st.error('Explore datasets')
    feature1, feature2 = st.columns([0.5, 0.4])
    with feature1:
        st.image(image1, use_column_width=True)
    with feature2:
        st.warning('Select features')
        st.info("""
                - Select features from dropdown menu
                - Select chart type for visualisation
                """)

    make_line()

    feature3, feature4 = st.columns([0.6, 0.4])
    with feature3:
        st.image(image2, use_column_width=True)
    with feature4:
        st.warning('Tweak Display')
        st.info("""
                - Pick *Dark/Light Theme*
                """)
    make_line()

    feature5, feature6 = st.columns([0.6, 0.4])
    with feature5:
        st.image(image3, use_column_width=True)
    with feature6:
        st.warning('Export')
        st.info("""
                - Save charts in different format
                """)

    make_line()

    return
