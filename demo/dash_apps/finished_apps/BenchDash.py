import pandas as pd #(version 0.24.2)
import datetime as dt
import dash
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
import plotly       #(version 4.4.1)
import plotly.express as px
import dash_labs as dl 
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import json
import numpy as np
from django_plotly_dash import DjangoDash
from dash_bootstrap_templates import load_figure_template
load_figure_template("superhero")


external_stylesheets = [dbc.themes.DARKLY]
app = DjangoDash('BenchDash', external_stylesheets=[external_stylesheets])

df = pd.read_csv("demo/static/Benchmark-2.csv")
dflt = pd.read_csv("demo/static/latest.csv")
df['Date']=pd.to_datetime(df['Date'])
df['Date'] = df['Date'].dt.strftime("%Y/%m/%d")
aggfuncs=['min']

max_val = df['Short%'].max().max()
sizes = [np.max([max_val/5, val]) for val in df['Short%'].values]
df['Index']=df['Short%']/df['Long%']
dfl = df.sort_values('Date').groupby('Name').tail(1)
fig = px.scatter(dfl, x='LongSpeed', y='ShortV', color='Name', range_color=[0.9, 1.1],
        labels={'x': 'Max Aerobic', 'y':'Max Speed'},
        hover_name='Date',
        hover_data=['Name','Long','Short'],
        color_continuous_scale='Plasma',
        size='compound',
        symbol='Class',
        )
fig.update_xaxes(range=[10, 17])
fig.update_layout(
    xaxis_title="MAS(1500/1250m)", 
    yaxis_title="Peak Speed(50m)",
    )

#dfl.to_csv('latest.csv')


app.layout = html.Div([

    html.H1(
        children='Benchmark Profile ',
    ),
    html.Div([
        html.Div([
        dcc.Graph(id='bench-graph',figure=fig),
        
        ],style={'width': '100%', 'display': 'inline-block', 'padding': '0 20'}),
    ]),
    html.Div([   
        html.Div([
            dcc.Graph(id='indiv-graph')
        ],style={'display': 'inline-block', 'width': '100%'}),      
    ]),
])

@app.callback(
    Output('indiv-graph', 'figure'),
    Input('bench-graph', 'clickData')
)
def update_graph(clickData):
    if not clickData:
        return dash.no_update
    athlete_name = clickData['points'][0]['customdata']

    dff = df[df['Name']== athlete_name[0]]
    dff=dff.sort_values(by='Date')
    fig = px.line(dff, x='Date', y=['PkV','ShortV', 'MedV','LongV'],labels={'x': 'Date', 'y':'Speed (m/s)'},
        hover_name='Date',
        hover_data=['Name','Long','Short', 'Med'],
        color_discrete_map={
            'LongV':'#0000CD',
            'DMedV':'#FFA500',
            'DShortV':'#FF0000',
            'DPkV':'#660066'},
        title= athlete_name[0],
        markers=True
            
        )
    fig.update_layout(
        xaxis={'categoryorder':'category ascending'},
        xaxis_title="Date", 
        yaxis_title="Speed (m/s)",
        margin={'b':60, 't':60})
    fig.update_xaxes(tickangle= -45)  

    return fig


