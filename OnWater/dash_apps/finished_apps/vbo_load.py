import re
import dash
from dash import Dash, dcc, html, Input, Output, dash_table, State
import plotly.graph_objects as go
import pandas as pd
import datetime
from datetime import datetime as dt
import base64
import io
from django_plotly_dash import DjangoDash
import os
from OnWater.dash_apps.finished_apps.vb3 import read_vbo
from OnWater.dash_apps.finished_apps import vb3

external_stylesheet =['https://codepen.io/chriddyp/pen/bWLwgP.css']
#app = dash.Dash(__name__, external_stylesheets=external_stylesheet)
app = DjangoDash('vbo_load', external_stylesheets=external_stylesheet)
app.layout = html.Div([
    html.H1('Upload a .vbo file', style={'text-align':'center'}),
    dcc.Upload(
        id='upload-data',
        children = html.Div([
            'Drag and Drop or ',
            html.A('Select a file')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle':'dashed',
            'borderRadius': '5px',
            'textalign' : 'centred',
            'margin': '10px'
        },
        multiple=True
    ),
    html.Div(id='output-data-upload')
])

def parse_contents(contents, filename, date):
    content_type, content_string=contents.split(',')

    decoded = base64.b64decode(content_string)
    try:
        if 'vbo' in filename:
            print('vbo found')
            df=pd.read_csv(
                io.StringIO(decoded.decode('utf-8')))
            os.makedirs('OnWater/folder/subfolder', exist_ok=True)    
            n = re.findall(r"^[ \w-]+", filename)
            name = str(n)[2:-2]
            fname = df.to_csv(f'OnWater//folder//subfolder//{name}.vbo', index=False)
            file = open(fname, 'rb')
            print(fname)
            print(type(file))
            #sdf = vb3.read_vbo(file)
            #print(name)
            #print('sent')
            #print(sdf.head)

        elif 'csv' in filename:
            df=pd.read_csv(
                io.StringIO(decoded.decode('utf-8'))
            )    
    except Exception as e:
        print(e)
        return html.Div([
            f'There was an error processing this file,  ---{e}'
        ])         
    

    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data = df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),
        html.Hr()

    ])

@app.callback(
    Output('output-data-upload', 'children'),
    [Input('upload-data', 'contents' )],
    [State('upload-data', 'filename'),
    State('upload-data', 'last_modified')]
)

def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        
        children = [
            parse_contents(c, n, d) for c, n, d in zip(list_of_contents, list_of_names, list_of_dates)
        ]
        return children        