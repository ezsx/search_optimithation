import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np
from points.points import Points_arr
from plot_fig.figure_build import plot_figure
from plot_fig.figure_build2 import plot_figure2
from utils.load_dir import load_dir

# Import all functions and algorithms

functions = load_dir("functions")
algorithms = load_dir("algorithms")

# Define the layout
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1('Optimization Visualization', className='main-title'),

        html.Div([
            dcc.Dropdown(id='function-dropdown',
                         options=[{'label': name, 'value': name} for name in functions.keys()],
                         value=list(functions.keys())[0],
                         className='dropdown'),
            dcc.Dropdown(id='algorithm-dropdown',
                         options=[{'label': name, 'value': name} for name in algorithms.keys()],
                         value=list(algorithms.keys())[0],
                         className='dropdown'),
            dcc.Dropdown(id='point-dropdown',
                         options=[{'label': str(point), 'value': i} for i, point in enumerate(Points_arr)],
                         value=0,
                         className='dropdown'),
        ], className='dropdowns-container'),
        html.Div([
            dcc.Textarea(id='output-area',
                         value='Output will be displayed here...',
                         readOnly=True,
                         className='output-area'),
        ], className='output-container'),
        html.Div([
            dcc.Graph(id='graph', className='graph'),
        ], className='graph-container'),
    ], className='main-container')


# Define the callback
@app.callback(
    Output('graph', 'figure'),
    Output('output-area', 'value'),
    Input('function-dropdown', 'value'),
    Input('algorithm-dropdown', 'value'),
    Input('point-dropdown', 'value')
)
def update_graph(function_name, algorithm_name, point_index):
    function = functions[function_name]
    algorithm = algorithms[algorithm_name]
    points = Points_arr[point_index]

    # Run the algorithm
    path, output = algorithm(function, points)

    # Create the figure
    fig = plot_figure(path, function)

    return fig, '\n'.join(output)


if __name__ == '__main__':
    app.run_server(debug=True)
