# script for file uploader and exploring data
import matplotlib.ticker as ticker
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import streamlit as st
from matplotlib import pyplot as plt

from script import ui_components as ui


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


def _setup(ax):
    ax.spines['right'].set_color('black')
    ax.spines['left'].set_color('black')
    ax.spines['top'].set_color('black')
    ax.spines['bottom'].set_color('black')

    ax.spines['right'].set_linewidth(0.3)
    ax.spines['left'].set_linewidth(0.3)
    ax.spines['top'].set_linewidth(0.3)
    ax.spines['bottom'].set_linewidth(0.3)

    ax.yaxis.set_major_locator(ticker.AutoLocator())
    ax.xaxis.set_ticks_position('bottom')

    ax.tick_params(which='major', width=1.00)
    ax.tick_params(which='major', length=5)
    ax.tick_params(which='minor', width=0.75)
    ax.tick_params(which='minor', length=2.5)
    # ax.set_xlim(0, 5)
    # ax.set_ylim(0, 1)
    ax.patch.set_alpha(0.0)

    return


def _plotly_update_layout(plot, feature1, feature2):
    """update the font size and type for plotly graphs"""
    plot.update_layout(
        # title="Plot Title",
        xaxis_title=feature1,
        yaxis_title=feature2,
        # legend_title="Legend Title",
        font=dict(
            family="Courier New, monospace",
            size=16,
            color="RebeccaPurple"
        )
    )


def _plot_update_rc():
    """update the rc fields of matplotlib"""
    rc = {'figure.figsize': (18, 4.5),
          'axes.facecolor': '#FFFFFF',  # 0e1117 - black
          'axes.edgecolor': '#FFFFFF',
          'axes.labelcolor': 'black',
          'figure.facecolor': '#FFFFFF',
          'patch.edgecolor': '#FFFFFF',
          'text.color': 'black',
          'xtick.color': 'black',
          'ytick.color': 'black',
          'grid.color': 'grey',
          'font.size': 8,
          'font.family': 'Courier New',
          'axes.labelsize': 8,
          'xtick.labelsize': 7,
          'ytick.labelsize': 7}

    plt.rcParams.update(rc)


def _matplotlib_figure(data, plot_num=1):
    """returns the axes for a matplotlib figure to further use for plotting"""
    _plot_update_rc()
    headers = data.columns
    if 'Unnamed: 0' in headers:
        headers = headers.drop('Unnamed: 0')

    subplot_col = 2
    subplot_row = 2

    fig = plt.figure()

    ax = fig.add_subplot(subplot_row, subplot_col, plot_num)

    return ax, fig


def _plot_data_line(df, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """line plots using plotly and seaborn"""
    if bCategorical:
        ax, fig = _matplotlib_figure(df, plot_num=1)
        sns.lineplot(data=df, x=feature1, y=feature2, hue=feature4, style=feature4)

        _setup(ax)
        plt.grid(True, linestyle='--', linewidth=0.4, color='#CFCFCF')
        st.pyplot(fig)

        ax, fig = _matplotlib_figure(df, plot_num=2)
        sns.lineplot(data=df, x=feature1, y=feature3, hue=feature4, style=feature4)

        _setup(ax)
        plt.grid(True, linestyle='--', linewidth=0.4, color='#CFCFCF')
        st.pyplot(fig)

        ax, fig = _matplotlib_figure(df, plot_num=3)
        sns.lineplot(data=df, x=feature2, y=feature3, hue=feature4, style=feature4)

        _setup(ax)
        plt.grid(True, linestyle='--', linewidth=0.4, color='#CFCFCF')
        st.pyplot(fig)

    else:
        plot = px.line(df,
                       x=feature1,
                       y=feature2,
                       markers=True,
                       color_discrete_sequence=px.colors.qualitative.Antique)
        plt.grid(True, linestyle='--', linewidth=0.4, color='#CFCFCF')
        st.plotly_chart(plot, use_container_width=True)


def _plot_data_bar(data, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """ plot bar chart for user selected columns"""

    def format_func(value, tick_number):
        """ return as string formatted """
        return "$%.2f$" % value

    if bCategorical:
        if chart_package == 'Seaborn':
            ax, fig = _matplotlib_figure(data)
            sns.barplot(x=feature1, y=feature2, data=data.round(2), hue=feature4, errcolor='black', errwidth=0.2,
                        color="#BEADE9", saturation=0.5, ax=ax)
        elif chart_package == 'Plotly':
            fig = px.bar(data, x=feature1, y=feature2, barmode='group', color=feature4,
                         color_discrete_sequence=px.colors.qualitative.Antique)
            fig.add_bar(x=data[feature1], y=data[feature3], name=feature3, marker_color='#F5F5F5')
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.75)
            fig.update_layout(hovermode="x unified")

            st.plotly_chart(fig, use_container_width=True)
    else:
        if feature1 is None or feature2 is None :
            st.write("""
            ***Please select both x and y axis features***
            """)
            return

        if chart_package == 'Seaborn':
            ax, fig = _matplotlib_figure(data)
            sns.barplot(x=feature1, y=feature2, data=data.round(2), errcolor='black', errwidth=0.2,
                        color="#BEADE9", saturation=0.5, ax=ax)

            _setup(ax)

            # ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))
            # ax.xaxis.set_major_formatter(ticker.FormatStrFormatter('%.2f'))
            ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
            ax.yaxis.set_major_locator(ticker.MaxNLocator(6))
            plt.grid(False)

            st.pyplot(fig)

        elif chart_package == 'Plotly':
            fig = px.bar(data, x=feature1, y=feature2, barmode='group',
                         color_discrete_sequence=px.colors.qualitative.Antique)
            fig.add_bar(x=data[feature1], y=data[feature3], name=feature3, marker_color='#F5F5F5')
            fig.update_layout(barmode='overlay')
            fig.update_traces(opacity=0.75)
            fig.update_layout(hovermode="x unified")

            st.plotly_chart(fig, use_container_width=True)

def _plot_data_histogram(df, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """plot histogram in plotly"""

    if bCategorical:
        plot1 = px.histogram(df,
                             x=feature1,
                             facet_col=feature3,
                             color=feature3,
                             histnorm='probability density',
                             color_discrete_sequence=px.colors.qualitative.Antique)

        plot2 = px.histogram(df,
                             x=feature2,
                             facet_col=feature3,
                             color=feature3,
                             histnorm='probability density',
                             color_discrete_sequence=px.colors.qualitative.Antique)

        plot3 = px.histogram(df,
                             x=feature4,
                             facet_col=feature3,
                             color=feature3,
                             histnorm='probability density',
                             color_discrete_sequence=px.colors.qualitative.Antique)

        st.plotly_chart(plot1, use_container_width=True)
        st.plotly_chart(plot2, use_container_width=True)
        st.plotly_chart(plot3, use_container_width=True)
    else:
        if feature1 is None or feature2 is None :
            st.write("""
            ***Please select both x and y axis features***
            """)
            return
        plot = go.Figure()
        plot.add_trace(go.Histogram(
            x=df[feature1],
            histnorm='probability density',
            showlegend=False,
            text=feature1,
            marker=dict(
                color='firebrick')
        ))
        plot.add_trace(go.Histogram(
            x=df[feature2],
            histnorm='probability density',
            showlegend=False,
            text=feature2,
            marker=dict(
                color='khaki')
        ))

        plot.update_layout(barmode='overlay')
        plot.update_traces(opacity=0.75)

        _plotly_update_layout(plot, ' & '.join([feature1, feature2]), 'probability density')

        st.plotly_chart(plot, use_container_width=True)


def _plot_data_scatter(data, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """scatter plot of selected data"""

    if bCategorical:
        plot = px.scatter(
            data_frame=data,
            x=feature1,
            y=feature2,
            color=feature4,
            size=feature3,
            # facet_col=feature3,
            hover_data=[feature3],
            # title="",
        )
    else:
        if feature1 is None or feature2 is None :
            st.write("""
            ***Please select both x and y axis features***
            """)
            return
        plot = go.Figure(data=go.Scatter(
            x=data[feature1],
            y=data[feature2],
            mode='markers',
            marker=dict(
                size=16,
                color=data[feature2],  # set color equal to a variable
                colorscale='Viridis',  # one of plotly colorscales
                showscale=True,
                colorbar=dict(
                    title=feature2,
                    borderwidth=0.1,
                    thickness=20
                )
            )
        ))

    _plotly_update_layout(plot, feature1, feature2)
    st.plotly_chart(plot, use_container_width=True)


def _plot_data_marginal(df, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """scatter plot with marginals of x and y axes data"""

    if bCategorical:
        plot = px.scatter(df,
                          x=feature1,
                          y=feature2,
                          color=feature4,
                          marginal_x="box",
                          marginal_y="violin",
                          color_discrete_sequence=px.colors.qualitative.Antique)

    else:
        if feature1 is None or feature2 is None :
            st.write("""
            ***Please select both x and y axis features***
            """)
            return
        plot = px.scatter(df,
                          x=feature1,
                          y=feature2,
                          marginal_x="histogram",
                          marginal_y="histogram",
                          color_discrete_sequence=px.colors.qualitative.Antique)

    _plotly_update_layout(plot, feature1, feature2)

    st.plotly_chart(plot, use_container_width=True)


def _plot_data_density_heatmap(df, feature1, feature2, feature3, feature4, bCategorical, chart_package):
    """plots density heatmap"""
    if bCategorical:
        plot = px.density_heatmap(df,
                                  x=feature1,
                                  y=feature2,
                                  z=feature3,
                                  facet_col=feature4,
                                  marginal_x="box",
                                  marginal_y="violin")
    else:
        if feature1 is None or feature2 is None :
            st.write("""
            ***Please select both x and y axis features***
            """)
            return
        plot = px.density_heatmap(df,
                                  x=feature1,
                                  y=feature2,
                                  marginal_x="box",
                                  marginal_y="violin")

    _plotly_update_layout(plot, feature1, feature2)

    st.plotly_chart(plot, use_container_width=True)


def _plot_data_corr_heatmap(df, feature1, feature3, bCategorical, chart_package):
    """show the correlation between features through heatmap"""
    ax, fig = _matplotlib_figure(df)
    if bCategorical:
        sns.heatmap(df.corr(),
                    annot=True,
                    linewidths=1,
                    )
    else:
        sns.heatmap(df.corr(),
                    annot=True,
                    linewidths=1,
                    )
    # _setup(ax)
    st.pyplot(fig)


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
    st.markdown("<h3 style='text-align: left; color: grey;'> \
                    Choose a csv file </h3>", unsafe_allow_html=True)

    file_path = 'data/Iris Dataset.csv'
    c1, c2 = st.columns((2, 1))
    with open(file_path, 'r') as f:
        dl_button = ui.download_button(f.read(), 'sample_file.txt', 'Try it out with my sample file!')
        c1.markdown(dl_button, unsafe_allow_html=True)

    uploaded_file = st.file_uploader('')
    if uploaded_file is not None:
        if '.csv' in uploaded_file.name or '.txt' in uploaded_file.name :
            df = pd.read_csv(uploaded_file)
        elif '.xlsx' in uploaded_file.name:
            df = pd.read_excel(uploaded_file)
        else:
            st.write("""
            ***Please upload a csv, excel or txt file***
            """)
            return

        st.write("""
        ***file uploaded successfully***
        """)

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

        st.write("""
        ***which features do you want to plot?***
        """)
        headers_mod = headers.append(pd.Index([None]))

        col3, col4, col5 = st.columns([1, 1, 1])

        feature1 = col3.selectbox(
            'select feature one - only numerical columns (x-axis):',
            headers_mod
        )
        col3.write(f"""
        `Selected feature - {feature1}`
        """)

        feature2 = col4.selectbox(
            'select feature two (y-axis):',
            headers_mod
        )
        col4.write(f"""
        `Selected feature - {feature2}`
        """)

        feature3 = col5.selectbox(
            'select a third feature - numerical (optional):',
            headers_mod
        )
        col5.write(f"""
        `Selected feature - {feature3}`
        """)

        col6, col7 = st.columns([1, 1])

        categorical = col6.selectbox(
            'Is it a categorical dataset?',
            ['No', 'Yes']
        )

        if categorical == 'Yes':

            feature4 = col7.selectbox(
                'select a categorical data column (optional):',
                headers_mod
            )
            col7.write(f"""
            `Selected categorical column - {feature4}`
            """)
        else:
            feature4 = None

        plot_types = (
            "Scatter",
            "Bar",
            "Histogram",
            "Marginal Distribution",
            'Density Heatmap',
            'Correlation Heatmap',
            "Line",
            "3D Scatter",
        )  # maybe add 'Boxplot'
        plot_packages = (
            "Plotly",
            "Seaborn",
        )
        # User choose type
        chart_type = st.selectbox("Choose your chart type", plot_types)
        chart_package = st.selectbox("Choose your plotting package", plot_packages)

        if chart_type == 'Scatter':
            _plot_data_scatter(df, feature1, feature2, feature3, feature4, True if categorical == 'Yes' else False,
                               chart_package)
        elif chart_type == 'Bar':
            _plot_data_bar(df, feature1, feature2, feature3, feature4, True if categorical == 'Yes' else False,
                           chart_package)
        elif chart_type == 'Histogram':
            _plot_data_histogram(df, feature1, feature2, feature3, feature4, True if categorical == 'Yes' else False,
                                 chart_package)
        elif chart_type == 'Marginal Distribution':
            _plot_data_marginal(df, feature1, feature2, feature3, feature4, True if categorical == 'Yes' else False,
                                chart_package)

        elif chart_type == 'Density Heatmap':
            _plot_data_density_heatmap(df, feature1, feature2, feature3, feature4,
                                       True if categorical == 'Yes' else False, chart_package)

        elif chart_type == 'Correlation Heatmap':
            _plot_data_corr_heatmap(df, feature1, feature2, True if categorical == 'Yes' else False, chart_package)

        elif chart_type == 'Line':
            _plot_data_line(df, feature1, feature2, feature3, feature4, True if categorical == 'Yes' else False,
                            chart_package)

        elif chart_type == '3D Scatter':
            st.write("""
            ***this plot type will be added soon***
            """)
