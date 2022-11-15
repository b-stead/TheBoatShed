from dash import Dash, dcc, html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate
import pandas as pd
import plotly.express as px
from django_plotly_dash import DjangoDash


dflt = pd.read_csv("demo/static/latest.csv")
options = [dflt['Name'], "Zoe Clark"
]
fig = px.bar(options, x="Date", y=['Short%', 'Med%', 'Long%'])


app = DjangoDash('benchprofile')
app.layout = html.Div([
    html.Div([
        "Benchmark Profile",
        dcc.Dropdown(id="my-dynamic-dropdown")
    ]),
    html.Div([
        "Graph",
        dcc.Graph(id="indiv-profile", figure=fig),
    ]),
])


@app.callback(
    Output("indiv-profile", "figure"),
    Input("my-dynamic-dropdown", "selected_value")
)
def update_options(selected_value):
    if not selected_value:
        raise PreventUpdate
    else: options = [dflt[selected_value]]
    return 
