import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np
from points.points import Points_arr
from plot_fig.figure_build import plot_figure
from utils.load_dir import load_dir

# Import all functions and algorithms

functions = load_dir("functions")
algorithms = load_dir("algorithms")

# Create a grid of points
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Define the layout
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1('Optimization Visualization', className='main-title'),
    dcc.Dropdown(id='function-dropdown', options=[{'label': name, 'value': name} for name in functions.keys()],
                 value=list(functions.keys())[0], className='dropdown'),
    dcc.Dropdown(id='algorithm-dropdown', options=[{'label': name, 'value': name} for name in algorithms.keys()],
                 value=list(algorithms.keys())[0], className='dropdown'),
    dcc.Dropdown(id='point-dropdown', options=[{'label': str(point), 'value': i} for i, point in enumerate(Points_arr)],
                 value=0, className='dropdown'),
    dcc.Textarea(id='output-area', value='Output will be displayed here...', style={'width': '100%'},
                 className='output-area'),
    dcc.Graph(id='graph', style={'height': '100vh', 'width': '100vw'}, className='graph'),

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
