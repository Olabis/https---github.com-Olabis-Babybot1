
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import pathlib
from dash import callback
# from app import app

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
dfv = pd.read_csv(DATA_PATH.joinpath("df2babybot.csv"))



# df = pd.read_csv("df2babybot.csv")



# app = dash.Dash()
# server= app.server

layout = html.Div(
    [
        html.Div([dcc.Graph(id="our_graph")]),
        html.Div(
            [
                html.Br(),
                html.Label(
                    ["Choose continent to compare:"],
                    style={"font-weight": "bold", "text-align": "center"},
                ),
                dcc.Dropdown(
                    id="Continents",
                    options=[
                        {"label": x, "value": x}
                        for x in dfv.sort_values("continent")["continent"].unique()
                    ],
                    value="African",
                    multi=False,
                    disabled=False,
                    clearable=True,
                    searchable=True,
                    placeholder="Choose continent...",
                    className="form-dropdown",
                    style={"width": "90%"},
                    persistence="string",
                    persistence_type="memory",
                ),
                dcc.RadioItems(id = 'graph-type',
                            options = [{'label': 'Scatter plot', 'value': 'scatter'},
                                      {'label': 'Line plot', 'value': 'line'}],
                             value = 'line'),
            ]
        ),
        html.H3("SUMMARY"),
        html.P(id= "Summary", children=["The graph above shows the Prevalence(frequency,rampancy) levels of countries with depression filtered by Continents. The average prevalence(%) according to WHO (World Health Organization) is 3.8%, this graph therefore shows countries across the world with their respective prevalence levels." ])
    ]
)


@callback(Output("our_graph", "figure"), 
                [Input("Continents", "value"), 
                Input("graph-type","value"),
                Input("Summary", "children")],
                suppress_callback_exceptions=True)
def update_figure(selected_continent,selected_graph,graph_summary):

    dff = dfv[(dfv["continent"] == selected_continent)]
    print(dff[:10])

    if selected_graph == "line":

        fig = px.line(dff, x="country", y="prevalence", color="continent", height=500)
        fig.update_layout(
        yaxis={"title": "Prevalence (%)"},
        xaxis={"title": "Countries"},
        title={
            "text": "Countries with depression in 2022",
            "font": {"size": 28},
            "x": 0.5,
            "xanchor": "center",
        },

    ),
    else:
        
        fig = px.scatter(dff,x="country", y="prevalence", color="continent", height=500)
        fig.update_layout(
        yaxis={"title": "Prevalence (%)"},
        xaxis={"title": "Countries"},
        title={
            "text": "Countries with depression in 2022",
            "font": {"size": 28},
            "x": 0.5,
            "xanchor": "center",})


    return fig


# if __name__ == "__main__":
#     app.run_server(debug=True)
# print('hi')
# print(dfv.head(10))