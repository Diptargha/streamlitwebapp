import pandas as pd
import streamlit as st
from streamlit_pandas_profiling import st_profile_report

from script import ui_components as ui


def _main(df):
    """includes items from the pandas profiling package"""

    # st.write("almost there...")
    # st_lottie(load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_m6cuL6.json"))

    pr = gen_profile_report(df, explorative=True)

    with st.expander("REPORT", expanded=True):
        st_profile_report(pr)


# @st.cache_data(allow_output_mutation=True)
@st.cache_data()
def gen_profile_report(df, *report_args, **report_kwargs):
    return df.profile_report(*report_args, **report_kwargs)


def run():
    st.title("Data profiler")
    st.write("""
       ## Select a file to explore the dataset
      """)
    st.markdown("<h3 style='text-align: left; color: grey;'> \
                      Choose a csv file </h3>", unsafe_allow_html=True)

    file_path = 'data/Iris Dataset.csv'
    c1, c2 = st.columns((2, 1))
    with open(file_path, 'r') as f:
        dl_button = ui.download_button(f.read(), 'sample_file.txt', 'Try it out with my sample file!')
        c1.markdown(dl_button, unsafe_allow_html=True)

    uploaded_file = st.file_uploader('')
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        headers = df.columns
        if 'Unnamed: 0' in headers:
            headers = headers.drop('Unnamed: 0')
        col1, col2 = st.columns([0.99, 0.01])

        with col1.expander('first few rows of data'):
            st.write("""
               `scroll to see more rows and columns`
              """)
            st.write(df)
        col2.write("""

          """)

        _main(df)
