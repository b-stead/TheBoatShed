from turtle import filling, title
import pandas as pd #(version 0.24.2)
from datetime import datetime, timedelta, datetime, date
from dash.dependencies import Input, Output
from dash import Dash, html, dcc
import plotly       #(version 4.4.1)
import plotly.express as px
import plotly.graph_objects as go
import dash_labs as dl 
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
from dash.exceptions import PreventUpdate
import numpy as np
from plotly.subplots import make_subplots
from .transform import f, calc, dates
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('Metrics', external_stylesheets=external_stylesheets)

#get data
df = pd.read_csv("athletes/static/AB_metrics_Oct.csv")

#import f and reassign names
df['Type']= df.apply(f, axis=1)
df=df[['Type','Timestamp','Value']]
df=df.rename(columns={"Type": "Metric"})

#multiply scores to convert to values out of ten
df['Score'] = df.apply(lambda x: calc(x['Value'], x['Metric']), axis=1)
df['Score'] = np.round(df.Score)
df = df.fillna(np.nan).replace([np.nan], [None])

#convert string time data in Timestamp column to datetime.date
df['Date'] = df.apply(lambda x: dates(x['Timestamp']), axis=1)

df = df.fillna(np.nan).replace([np.nan], [None])

#Build page for dashboard

app.layout = html.Div([
    html.Div([
       
        html.Div([
            dcc.Dropdown(
                df['Metric'].unique(), 'Fatigue',
                id = 'primary',
            )
        ], style={'display':'inline-block', 'marginTop': '5px', 'width': '24%'}
        ),
        html.Div([
            dcc.Dropdown(
                df['Metric'].unique(), 'Feeling',
                id = 'secondary',
            )
        ], style={'display':'inline-block', 'marginTop': '5px', 'width': '24%'}
        ),
        html.Div([
            dcc.Dropdown(
                df['Metric'].unique(), 'Pulse',
                id = 'tertiary',
            )
        ], style={'display':'inline-block', 'marginTop': '5px', 'width': '24%'}
        ),
        html.Div([
            dcc.Dropdown(
                df['Metric'].unique(), 'Stress',
                id = 'quartenary',
            )
        ], style={'display':'inline-block', 'marginTop': '5px', 'width': '24%'}
        ),
    ]),
    html.Div([
            html.Div([
                dcc.Graph(id='metrics-graph1', style={'display': 'inline-block'}),
                dcc.Graph(id='metrics-graph2', style={'display': 'inline-block'})
            ]),
        ])

])

@app.callback(
    Output('metrics-graph1', 'figure'),
    Output('metrics-graph2', 'figure'),
    Input('primary', 'value'),
    Input('secondary', 'value'),
    Input('tertiary', 'value'),
    Input('quartenary', 'value'),
)
def create_time_series(primary, secondary, tertiary, quartenary):
    
    
    df1 = df[df['Metric'] == primary]
    df2 = df[df['Metric'] == secondary]
    df3 = df[df['Metric'] == tertiary]
    df4 = df[df['Metric'] == quartenary]

    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(
        x=df1['Date'],
        y=df1['Score'],
        name = primary,
        connectgaps=True),
        secondary_y=False,
        ),
    fig.add_trace(go.Scatter(
        x=df2['Date'],
        y=df2['Score'],
        name = secondary,
        connectgaps=True),
        secondary_y=True,
        )

    fig2 = make_subplots(specs=[[{"secondary_y": True}]])
    fig2.add_trace(go.Scatter(
        x=df3['Date'],
        y=df3['Score'],
        name = tertiary,
        connectgaps=True),
        secondary_y=False,
        ),
    fig2.add_trace(go.Scatter(
        x=df4['Date'],
        y=df4['Score'],
        name = quartenary,
        connectgaps=True),
        secondary_y=True,
        )
    
    
    # Add range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list([
                    dict(count=1,
                        label="1m",
                        step="month",
                        stepmode="backward"),
                    dict(count=6,
                        label="6m",
                        step="month",
                        stepmode="backward"),
                    dict(count=1,
                        label="YTD",
                        step="year",
                        stepmode="todate"),
                    dict(count=1,
                        label="1y",
                        step="year",
                        stepmode="backward"),
                    dict(step="all")
                ])
            ),
            rangeslider=dict(
                visible=True
            ),
            type="date"
        )
    )
    
    return fig, fig2

