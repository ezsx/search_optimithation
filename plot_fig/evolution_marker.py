import numpy as np
import plotly.graph_objects as go


def plot_evolution(populations, f, color_scale='rdbu', x_range=(-5, 5), y_range=(-5, 5)):
    """
    Plots and animates the evolution of populations on a 3D surface representing the function f.

    :param populations: A list of populations, each population is an array of points.
    :param f: The function to be optimized.
    :param x_range: The range of x values for the surface plot.
    :param y_range: The range of y values for the surface plot.
    :param color_scale: Color scale for the surface plot.
    :return: Plotly figure object.
    """

    # Create a grid of points for the surface plot
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each grid point
    z = np.array([f([x_point, y_point]) for x_point, y_point in zip(x.flatten(), y.flatten())])
    z = z.reshape(x.shape)

    # Create the surface plot of the function
    function_surface = go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8)

    # Define frames
    frames = [
        go.Frame(
            data=[
                function_surface,
                go.Scatter3d(
                    x=population[:, 0], y=population[:, 1],
                    z=[f(individual) for individual in population],
                    mode='markers',
                    marker=dict(size=5),
                    name=f'Step {k}')
            ],
            name=str(k)
        )
        for k, population in enumerate(populations)
    ]

    # Define slider and buttons
    sliders = [{
        "steps": [
            {
                "method": "animate",
                "args": [
                    [str(k)],
                    {
                        "frame": {"duration": 300, "redraw": True},
                        "mode": "immediate",
                        "transition": {"duration": 300}
                    }
                ],
                "label": str(k)
            } for k in range(len(populations))
        ],
        "active": 0,
        "currentvalue": {"prefix": "Step: "}
    }]

    buttons = [{"type": "buttons",
                "showactive": False,
                "buttons": [{"label": "▶",
                             "method": "animate",
                             "args": [None, {
                                 "frame": {"duration": 200, "redraw": True},
                                 "fromcurrent": True,
                                 "transition": {"duration": 100,
                                                "easing": "quadratic-in-out"}}]},
                            {"label": "❚❚",
                             "method": "animate",
                             "args": [[None], {"frame": {"duration": 0, "redraw": False},
                                               "mode": "immediate",
                                               "transition": {"duration": 0}}]}]}]

    # Layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(range=[x_range[0], x_range[1]]),
            yaxis=dict(range=[y_range[0], y_range[1]]),
            zaxis=dict(range=[np.min(z), np.max(z)])
        ),
        updatemenus=buttons,
        sliders=sliders
    )

    # Create initial figure
    fig = go.Figure(
        data=[function_surface] +
             [go.Scatter3d(
                 x=populations[0][:, 0], y=populations[0][:, 1],
                 z=[f(individual) for individual in populations[0]],
                 mode='markers',
                 marker=dict(size=5),
                 name='Step 0')
             ],
        frames=frames,
        layout=layout
    )

    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    fig.update_layout(modebar=dict(bgcolor="rgba(0,0,0,0)"))

    return fig
