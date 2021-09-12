# script for file uploader and exploring data
import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import plotly.express as px
from itertools import combinations


def display_mode(plot_mode):
    """ rcParameters for light and dark mode """

    if plot_mode == 'Dark Mode':
        colors = {
            'pdf_line_color': '#fec44f',
            'hist_color': '#bdbdbd',
            'hist_edge_color': 'grey',
            'cdf_line_color': 'white',
            'frame_edge_color': '#525252',
            'boxplot_lines_color': 'white',
            'boxplot_face_color': 'black',
            'quant1_color': '#c7e9b4',
            'quant2_color': '#7fcdbb',
            'quant3_color': '#41b6c4',
        }

    if plot_mode == 'Light Mode':
        colors = {
            'pdf_line_color': '#08519c',
            'hist_color': '#525252',
            'hist_edge_color': 'grey',
            'cdf_line_color': 'black',
            'frame_edge_color': '#525252',
            'boxplot_lines_color': 'black',
            'boxplot_face_color': 'white',
            'quant1_color': '#b2182b',
            'quant2_color': '#35978f',
            'quant3_color': '#b35806',
        }

    if plot_mode == 'Dark Mode':
        plt.style.use('dark_background')
        plt.rcParams['figure.facecolor'] = 'black'

    if plot_mode == 'Light Mode':
        plt.style.use('classic')
        plt.rcParams['figure.facecolor'] = 'white'


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
    return


def _plot_data_bar(data, feature1, feature2):
    """ plot bar chart for user selected columns"""

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


def _plot_data_scatter(data, feature1, feature2):
    """scatter plot of selected data"""

    plot = px.scatter(
        data_frame=data,
        x=feature1,
        y=feature2,
        # color="species",
        # title="",
    )

    st.plotly_chart(plot, use_container_width=True)


def make_expanders(expander_name, sidebar=True):
    """ Set up expanders which contains a set of options. """
    if sidebar:
        try:
            return st.sidebar.expander(expander_name)
        except:
            return st.sidebar.beta_expander(expander_name)


def run():
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
            'select feature one (x-axis):',
            headers
        )
        col3.write(f"""
        `Selected feature - {feature1}`
        """)

        feature2 = col4.selectbox(
            'select feature two (y-axis):',
            headers
        )
        col4.write(f"""
        `Selected feature - {feature2}`
        """)

        # Figure display properties expander
        # with make_expanders("Tweak display"):
        #
        #     st.markdown("**Select Figure Mode:**")
        #     plot_mode = st.radio("Options", ('Dark Mode', 'Light Mode'))
        #
        # display_mode(plot_mode)

        plot_types = (
            "Scatter",
            "Histogram",
            "Bar",
            "Line",
            "3D Scatter",
        )  # maybe add 'Boxplot'

        # User choose type
        chart_type = st.selectbox("Choose your chart type", plot_types)

        if chart_type == 'Scatter':
            _plot_data_scatter(df, feature1, feature2)
        elif chart_type == 'Bar':
            _plot_data_bar(df, feature1, feature2)
        elif chart_type == 'Histogram':
            st.write("""
            ***this plot type will be added soon***
            """)

        elif chart_type == 'Line':
            st.write("""
            ***this plot type will be added soon***
            """)

        elif chart_type == '3D Scatter':
            st.write("""
            ***this plot type will be added soon***
            """)
