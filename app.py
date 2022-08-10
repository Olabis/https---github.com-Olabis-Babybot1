import dash
import dash_labs as dl  
import dash_bootstrap_components as dbc 

#Initialize app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server
