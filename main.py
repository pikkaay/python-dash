import dash
from dash.dependencies import Output, Event
import dash_core_components as dcc
import dash_html_components as html
import plotly as py 
import random
import plotly.graph_objs as go
from collections import deque
import datetime

print(dash.__version__)
print(py.__version__)
# py.offline.init_notebook_mode(connected=True)


start = datetime.datetime.now() - datetime.timedelta(seconds=30) + datetime.timedelta(hours=5, minutes = 30)
X = deque(maxlen=600)
X.append(start)
for i in range(600):
    X.append(X[-1]+datetime.timedelta(seconds=1))

Y = deque(maxlen=20)
Y.append(1)
for i in range(20):
    Y.append(Y[-1]+1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=2000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              events=[Event('graph-update', 'interval')])
def update_graph_scatter():
        

    X.append(X[-1]+datetime.timedelta(seconds=1))
    Y.append(Y[-1]+1)

    data = py.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )

    return {'data': [data],'layout' : py.graph_objs.Layout(
        # xaxis=dict(range=[min(X),max(X)+5]),
                                                yaxis=dict(range=[min(Y),max(Y)]),)}

if __name__ == '__main__':
    app.run_server(debug=True)