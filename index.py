import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from app import server

from pages import prevalence_continent, prevalence_year

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('2022prevalence|', href='/pages/prevalence_continent'),
        dcc.Link('Prevanlencethr_years', href='/pages/prevalence_year'),
    ], className="row"),

    # dcc.Location(id='url', refresh=False),
    html.Div(id='page-content', children=[])
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])

def display_page(pathname):
    if pathname == '/pages/prevalence_continent':
        return prevalence_continent.layout
    if pathname == '/pages/prevalence_year':
        return prevalence_year.layout
    else:
        return  "Please choose a link"




if __name__ == "__main__":
    app.run_server(debug=True)