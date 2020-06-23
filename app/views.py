import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import dash_table as dt
from . import env
from dash.dependencies import Input, Output


def dashboard(server):
    external_stylesheet = env.css_url
    dash_app = dash.Dash(__name__, server=server,
                         external_stylesheets=external_stylesheet, url_base_pathname="/dashboard/")
    return dash_app.server
