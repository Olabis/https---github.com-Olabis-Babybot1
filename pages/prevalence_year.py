
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash import callback
from dash.dependencies import Input, Output
import pathlib
# from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
dfy = pd.read_csv(DATA_PATH.joinpath("number-with-depression-by-country (1).csv")) 


def graph_region(region_df, graph_type: str, dimension1: str, dimension2: str):
    
    """
    Parameters
    ------------
        region_df: (dataframe object)
        graph_type: (string) "bar", "scatter", "line"
        dimension1: (str) one of 'Year'
        dimension2: (str) one of 'Prevalence'
        
    Returns:
    -----------
        plotly figure
    """
    
    plot_dict = {'scatter': px.scatter, 'line': px.line}
    
    try:
        #initialize function
        fig = plot_dict[graph_type](region_df,
                                   x = dimension1,
                                   y = dimension2,
                                   color = "Entity")
        
        #format figure
        title_string = f'Chart: {graph_type} of {dimension1} and {dimension2} by Entity'
        fig.update_layout(title = title_string)
        return fig
    
    except KeyError:
        print("Key not found")
    except ValueError:
        print("Value is invalid")
        
#-----------------------------------------------------------------#

#read data
# spreadsheet = pd.read_csv('number-with-depression-by-country.csv')

#----------------------------------------------------------------#
#App section

# Stylesheets
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

#Initialize app
# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# server = app.server

layout = html.Div([
                html.H1("Depression graphs"),
                dcc.Dropdown(id='Province',
                            options=[{'label': i, 'value': i} for i in dfy['Entity'].unique()],
                            value = 'Nigeria'),
                dcc.RadioItems(id = 'graph-type',
                            options = [{'label': 'Scatter plot', 'value': 'scatter'},
                                      {'label': 'Line plot', 'value': 'line'}],
                             value = 'line'),
                dcc.Graph('graph-render'),

                html.H3("SUMMARY"),
                html.P(id="Summary", children=["The graph above shows the prevalence (number of people suffering from depression) level of different countries through the years varying from the year 1990 to the year 2020. "])
                    ])
@callback(
    Output('graph-render', 'figure'),
    Input('graph-type', 'value'),
    Input('Province', 'value'),
    Input('Summary','children'),
    suppress_callback_exceptions=True)
def update_figure0(selected_graph, selected_province, graph_summary):
    df =dfy #spreadsheet
    filtered_df = df[df['Entity'] == selected_province]
    fig0 = graph_region(filtered_df, selected_graph, "Year", "Prevalence")
    return fig0

    fig = px.scatter(filtered_df,
                                x = 'Year',
                                y = 'Prevalence',
                                color = "Entity")
    
    #format figure
    # title_string = f'Chart: {graph_type} of {dimension1} and {dimension2} by Entity'
    # fig.update_layout(title = title_string)
    return fig



# if __name__ == '__main__':
#     app.run_server(debug=True)
