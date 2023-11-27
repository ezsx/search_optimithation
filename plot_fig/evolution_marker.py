import numpy as np
import plotly.graph_objects as go
from utils.base_plot_parametrs import base_slider, base_buttons


def plot_evolution(populations, f, color_scale='rdbu', color_point="black", x_range=(-5, 5), y_range=(-5, 5)):
    """
    Plots and animates the evolution of populations on a 3D surface representing the function f.

    :param populations: A list of populations, each population is an array of points.
    :param f: The function to be optimized.
    :param x_range: The range of x values for the surface plot.
    :param y_range: The range of y values for the surface plot.
    :param color_scale: Color scale for the surface plot.
    :param color_point: Color of the points in the population.
    :return: Plotly figure object.
    """

    # Create a grid of points for the surface plot
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each grid point
    z = f([x, y])

    # Create the surface plot of the function
    function_surface = go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8)

    # Define frames with a special color for the lowest z point
    frames = []
    for k, population in enumerate(populations):
        # Evaluate the function for the current population
        z_values = np.array([f(individual) for individual in population])

        # Find the index of the lowest z value
        min_z_index = np.argmin(z_values)

        # Prepare marker colors, set the color for the minimum point
        marker_colors = [color_point] * len(population)
        marker_colors[min_z_index] = 'gold'  # Highlight the lowest point with gold color
        # changing size of lowest point
        marker_size = [18] * len(population)
        marker_size[min_z_index] = 30

        frame = go.Frame(
            data=[
                function_surface,
                go.Scatter3d(
                    x=population[:, 0], y=population[:, 1], z=z_values,
                    mode='markers',
                    marker=dict(size=marker_size, color=marker_colors),
                    name=f'Step {k}'
                )
            ],
            name=str(k)
        )
        frames.append(frame)

    # Define slider and buttons
    sliders = base_slider(frames)
    buttons = base_buttons()

    # Define the camera settings for a consistent view

    # Layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(range=[x_range[0], x_range[1]]),
            yaxis=dict(range=[y_range[0], y_range[1]]),
            zaxis=dict(range=[np.min(z)-1, np.max(z)]),
        ),
        updatemenus=buttons,
        sliders=sliders,
    )

    # Create initial figure with a special color for the lowest z point in the first population
    initial_z_values = np.array([f(individual) for individual in populations[0]])
    initial_min_z_index = np.argmin(initial_z_values)
    initial_marker_colors = [color_point] * len(populations[0])
    initial_marker_colors[initial_min_z_index] = 'gold'  # Highlight the lowest point with gold color
    # changing size of lowest point
    initial_marker_size = [18] * len(populations[0])
    initial_marker_size[initial_min_z_index] = 30

    fig = go.Figure(
        data=[function_surface] +
             [go.Scatter3d(
                 x=populations[0][:, 0], y=populations[0][:, 1], z=initial_z_values,
                 mode='markers',
                 marker=dict(size=initial_marker_size, color=initial_marker_colors),
                 name='Step 0')
             ],
        frames=frames,
        layout=layout
    )

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), modebar=dict(bgcolor="rgba(0,0,0,0)"))
    # dark theme
    # fig.update_layout(template="plotly_dark")
    # automargin=True
    fig.update_layout(autosize=True)
    return fig
