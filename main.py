import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np
from base.points import Points_arr
from base.plot_fig.figure_1 import plot_figure
from base import functions
from base.algorithms.gradient_descent import GradientDescent
from base.algorithms.quadratic_programming import QuadraticProgramming
from base.functions import himmelblau
from base.algorithms.algorithm_type import AlgorithmType


functions = {
    'himmelblau': himmelblau
}

algorithms: {str: AlgorithmType} = {
    'gradient descent': AlgorithmType.gradient_descent,
    'quadratic programming': AlgorithmType.quadratic_programming
}

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
    algorithm_type: AlgorithmType = algorithms[algorithm_name]
    points = Points_arr[point_index]

    # Run the algorithm
    algorithm = algorithm_type.get_algorithm(function, points)
    path = algorithm.solve()
    # Create the figure
    return plot_figure(path, function)


if __name__ == '__main__':
    app.run_server(debug=True)
