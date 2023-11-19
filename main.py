import json

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import numpy as np
from points.points import Points_dict
from plot_fig.path_tracer import plot_traces
from plot_fig.evolution_marker import plot_evolution
from utils.load_dir import load_dir
import plotly

# Import all functions and algorithms

functions = load_dir("functions")
algorithms = load_dir("algorithms")
# plot_fig = load_dir("plot_fig")

color_scales = plotly.colors.named_colorscales()
color_points = {"black": "black", "gold": "gold", "blue": "blue", "green": "green", "yellow": "yellow", "red": "red",
                "white": "white"}

# Define the layout
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1('Optimization Visualization', className='main-title'),
        html.Div([], className='inherted-container'),
        html.Div([
            dcc.Dropdown(id='function-dropdown',
                         options=[{'label': "function: " + name, 'value': name} for name in functions.keys()],
                         value="himmelblau",
                         clearable=False,
                         className='dropdown'),
            dcc.Dropdown(id='algorithm-dropdown',
                         options=[{'label': "algorithm: " + name, 'value': name} for name in algorithms.keys()],
                         value=list(algorithms.keys())[0],
                         clearable=False,
                         className='dropdown'),
            dcc.Dropdown(id='point-dropdown',
                         options=[{'label': "point set: " + name, 'value': name} for name in Points_dict.keys()],
                         clearable=False,
                         value=list(Points_dict.keys())[0],
                         className='dropdown'),
            dcc.Dropdown(id='color-scale-dropdown',
                         options=[{'label': "plot color: " + name, 'value': name} for name in color_scales],
                         value='rdbu',
                         clearable=False,
                         className='dropdown'
                         ),
            dcc.Dropdown(id='point-color-dropdown',
                         options=[{'label': "point color: " + name, 'value': name} for name in color_points.keys()],
                         clearable=False,
                         value=list(color_points.keys())[0],
                         className='dropdown'),
            html.Button('Update Camera Position', id='update-camera-btn'),
        ], className='dropdowns-container'),
        html.Div([
            dcc.Textarea(id='output-area',
                         value='Output will be displayed here...',
                         readOnly=True,
                         className='output-area'),
        ], className='output-container'),

        html.Div([
            dcc.Graph(id='graph', className='graph', config={
                'displayModeBar': False,
                'modeBarButtonsToRemove': ['toImage', 'sendData', 'autoScale2d', 'resetScale2d']
            }),
        ], id='graph-container', className='graph-container'),
        html.Div(id='camera-data', style={'display': 'none'})

    ], className='main-container')

# Clientside callback to store the camera position
app.clientside_callback(
    """
    function(relayoutData) {
        if(relayoutData && relayoutData['scene.camera']) {
            return JSON.stringify(relayoutData['scene.camera']);
        }
        return null;
    }
    """,
    Output('camera-data', 'children'),
    [Input('graph', 'relayoutData')]
)


# Define the server-side callback for graph updates
@app.callback(
    Output('graph', 'figure'),
    Output('output-area', 'value'),
    [Input('update-camera-btn', 'n_clicks'),
     Input('function-dropdown', 'value'),
     Input('algorithm-dropdown', 'value'),
     Input('point-dropdown', 'value'),
     Input('color-scale-dropdown', 'value'),
     Input('point-color-dropdown', 'value')],
    [State('camera-data', 'children')]

)
def update_graph(n_clicks, function_name, algorithm_name, point_index, color_scale, point_color,
                 stored_camera_data):
    function = functions[function_name]
    algorithm = algorithms[algorithm_name]
    points = Points_dict[point_index]
    point_color = color_points[point_color]

    # Run the algorithm
    path, output = algorithm(function, points)
    plot_figure = None

    # choose plot function logic
    match algorithm_name:
        case 'genetic_algorithm':
            plot_figure = plot_evolution
        case 'particle_swarm_optimization':
            plot_figure = plot_evolution
        case 'bee_swarm_optimization':
            plot_figure = plot_evolution
        case 'immune_network_optimization':
            plot_figure = plot_evolution
        case 'gradient_descent':
            plot_figure = plot_traces
        case 'quadratic_programming':
            plot_figure = plot_traces
        case _:
            raise ValueError(f"Algorithm {algorithm_name} is not supported.")

    # Create the figure
    fig = plot_figure(path, function, color_scale, point_color)

    # Apply the stored camera data if available
    print(stored_camera_data)
    if stored_camera_data:
        current_camera = json.loads(stored_camera_data)
        fig.update_layout(scene_camera=current_camera)
    else:
        # Define a default camera view or handle the null case appropriately
        default_camera = dict(eye=dict(x=1.25, y=1.25, z=1.25), up=dict(x=0, y=0, z=1))
        fig.update_layout(scene_camera=default_camera)

    # print(path)
    return fig, str(output)


if __name__ == '__main__':
    app.run_server(debug=True)

# TODO:
#  1) add just 2 algorithms
#  2) add some more functions
#  3) add documentation to algorithms
# DONE:
#  3) custom placeholder, output, title, button design
