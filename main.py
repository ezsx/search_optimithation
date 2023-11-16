import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
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

# Define the layout
app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1('Optimization Visualization', className='main-title'),
        html.Div([], className='inherted-container'),
        html.Div([
            dcc.Dropdown(id='function-dropdown',
                         options=[{'label': name, 'value': name} for name in functions.keys()],
                         value=list(functions.keys())[0],
                         clearable=False,
                         className='dropdown'),
            dcc.Dropdown(id='algorithm-dropdown',
                         options=[{'label': name, 'value': name} for name in algorithms.keys()],
                         value=list(algorithms.keys())[0],
                         clearable=False,
                         className='dropdown'),
            dcc.Dropdown(id='point-dropdown',
                         options=[{'label': name, 'value': name} for name in Points_dict.keys()],
                         clearable=False,
                         value=list(Points_dict.keys())[0],
                         className='dropdown'),
            dcc.Dropdown(id='color-scale-dropdown',
                         options=color_scales,
                         value='rdbu',
                         clearable=False,
                         className='dropdown'
                         ),
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
        ], className='graph-container'),

    ], className='main-container')


# Define the callback
@app.callback(
    Output('graph', 'figure'),
    Output('output-area', 'value'),
    Input('function-dropdown', 'value'),
    Input('algorithm-dropdown', 'value'),
    Input('point-dropdown', 'value'),
    Input('color-scale-dropdown', 'value')

)
def update_graph(function_name, algorithm_name, point_index, color_scale):
    function = functions[function_name]
    algorithm = algorithms[algorithm_name]
    points = Points_dict[point_index]

    # Run the algorithm
    path, output = algorithm(function, points)
    plot_figure = None

    # choose plot function logic
    match algorithm_name:
        case 'genetic_algorithm':
            plot_figure = plot_evolution
        case 'particle_swarm_optimization':
            plot_figure = plot_evolution
        case 'gradient_descent':
            plot_figure = plot_traces
        case 'quadratic_programming':
            plot_figure = plot_traces
        case _:
            raise ValueError(f"Algorithm {algorithm_name} is not supported.")

    # Create the figure
    fig = plot_figure(path, function, color_scale)

    print(path)
    return fig, str(output)


if __name__ == '__main__':
    app.run_server(debug=True)
