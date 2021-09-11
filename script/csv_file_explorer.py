# script for file uploader and exploring data
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
from itertools import combinations


def plot_data(data, feature1, feature2):
    """ plot user selected columns"""

    def setup(ax):
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.yaxis.set_major_locator(ticker.AutoLocator())
        ax.spines['top'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.xaxis.set_ticks_position('bottom')
        ax.tick_params(which='major', width=1.00)
        ax.tick_params(which='major', length=5)
        ax.tick_params(which='minor', width=0.75)
        ax.tick_params(which='minor', length=2.5)
        # ax.set_xlim(0, 5)
        # ax.set_ylim(0, 1)
        ax.patch.set_alpha(0.0)

    def format_func(value, tick_number):
        """ return as string formatted """
        return "$%.2f$" % value

    rc = {'figure.figsize': (18, 4.5),
          'axes.facecolor': '#0e1117',
          'axes.edgecolor': '#0e1117',
          'axes.labelcolor': 'white',
          'figure.facecolor': '#0e1117',
          'patch.edgecolor': '#0e1117',
          'text.color': 'white',
          'xtick.color': 'white',
          'ytick.color': 'white',
          'grid.color': 'grey',
          'font.size': 8,
          'axes.labelsize': 8,
          'xtick.labelsize': 5,
          'ytick.labelsize': 5}
    plt.rcParams.update(rc)
    headers = data.columns
    if 'Unnamed: 0' in headers:
        headers = headers.drop('Unnamed: 0')
    columns = list(combinations(headers, 2))
    subplot_col = 2
    # subplot_row = round(len(columns) / subplot_col)
    subplot_row = 2
    fig = plt.figure()
    plot_num = 1

    # for col in columns:
    ax = fig.add_subplot(subplot_row, subplot_col, plot_num)

    # sns.barplot(x=col[0], y=col[1], data=data, color="#b80606", ax=ax)
    sns.barplot(x=feature1, y=feature2, data=data.round(2), color="salmon", saturation=0.5, ax=ax)
    setup(ax)

    # ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))
    # ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax.yaxis.set_major_locator(ticker.MaxNLocator(6))
    plt.grid(False)

    st.pyplot(fig)


def run():
    st.set_page_config(layout="wide")
    st.title("Data explorer")
    st.write("""
     ## Select a file to explore the dataset
    """)

    uploaded_file = st.file_uploader("Choose a csv file")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        headers = df.columns
        if 'Unnamed: 0' in headers:
            headers = headers.drop('Unnamed: 0')
        col1, col2 = st.columns([1, 1])

        with col1.expander('first 10 rows of the data'):
            st.write("""
             `scroll to see more rows and columns`
            """)
            st.write(df)
        col2.write("""
        
        """)

        st.write("""
        ***which features do you want to plot?***
        """)

        col3, col4 = st.columns([1, 1])

        feature1 = col3.selectbox(
            'select feature one:',
            headers
        )
        col3.write(f"""
        `Selected feature - {feature1}`
        """)

        feature2 = col4.selectbox(
            'select feature two:',
            headers
        )
        col4.write(f"""
        `Selected feature - {feature2}`
        """)

        plot_data(df, feature1, feature2)
