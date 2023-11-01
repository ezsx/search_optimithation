import os
import importlib
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import numpy as np
from points.points import Points_arr
from plot_fig.figure_1 import plot_figure

# Import all functions and algorithms
# Import all functions and algorithms
functions = {os.path.splitext(file)[0]: importlib.import_module(f'functions.{os.path.splitext(file)[0]}').__dict__[
    os.path.splitext(file)[0]] for file in os.listdir('functions') if os.path.isfile(f'functions/{file}') and file.endswith('.py')}
algorithms = {os.path.splitext(file)[0]: importlib.import_module(f'algorithms.{os.path.splitext(file)[0]}').__dict__[
    os.path.splitext(file)[0]] for file in os.listdir('algorithms') if os.path.isfile(f'algorithms/{file}') and file.endswith('.py')}


# Create a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define the layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Optimization Visualization'),
    dcc.Dropdown(id='function-dropdown', options=[{'label': name, 'value': name} for name in functions.keys()],
                 value=list(functions.keys())[0]),
    dcc.Dropdown(id='algorithm-dropdown', options=[{'label': name, 'value': name} for name in algorithms.keys()],
                 value=list(algorithms.keys())[0]),
    dcc.Dropdown(id='point-dropdown', options=[{'label': str(point), 'value': i} for i, point in enumerate(Points_arr)],
                 value=0),
    dcc.Graph(id='graph')
])


# Define the callback
@app.callback(
    Output('graph', 'figure'),
    Input('function-dropdown', 'value'),
    Input('algorithm-dropdown', 'value'),
    Input('point-dropdown', 'value')
)
def update_graph(function_name, algorithm_name, point_index):
    function = functions[function_name]
    algorithm = algorithms[algorithm_name]
    points = Points_arr[point_index]

    # Run the algorithm
    path = algorithm(function, points)

    # Create the figure
    fig = plot_figure(path, function)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
