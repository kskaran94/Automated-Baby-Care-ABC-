import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import datetime
from datetime import timedelta
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

x = np.arange(0,100,1)
time = datetime.datetime.now()
t =[]
for i in range(len(x)) :
   t.append(time + timedelta(seconds = x[i]))
y = ['Not Crying' for i in range(20)]
y = y + ['Crying' for i in range(60)]
y = y + ['Not Crying' for i in range(10)]
y = y + ['Crying' for i in range(10)]
ny = np.array(y)
d = {'x':list(t),'y':list(y)}
df = pd.DataFrame(data=d)


app.layout = html.Div([

    html.H1(
        children='Baby Sleep Analysis',
        style={
            'textAlign': 'center',
        }
    ),


    dcc.Graph(
        id='1',
        figure={
            'data': [
                go.Scatter(
                    x=df['x'],
                    y=df['y'],
                    #text=df[df['x'] == i]['x'],
                    mode='lines',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    

                ) 
            ],
            'layout': go.Layout(
                xaxis={'title': 'Time'},
                yaxis={'title': 'Crying status'},
                margin={'l': 100, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ),

    dcc.Graph(
        id='2',
        figure={
            'data': [
        {
            'labels': ['crying' , 'not crying'],
            'values': [40, 60],
            'type': 'pie',
           
        },
        ] } )

    ])

if __name__ == '__main__':
    app.run_server(port=8050,debug=True)