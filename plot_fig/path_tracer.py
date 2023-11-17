import numpy as np
import plotly.graph_objects as go

from utils.base_plot_parametrs import base_slider, base_buttons


def plot_traces(paths, f, color_scale='rdbu', color_point='gold', x_range=(-5, 5), y_range=(-5, 5)):
    """
    not wrote yet
    """
    # Create a grid of points
    x = np.linspace(x_range[0], x_range[1], 100)
    y = np.linspace(y_range[0], y_range[1], 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each point
    z = f([x, y])

    # Define frames
    frames = [go.Frame(
        data=[go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8, showscale=False)] +

             [go.Scatter3d(x=path[:k + 1, 0], y=path[:k + 1, 1], z=[f(x) for x in path[:k + 1]],
                           mode='lines+markers',
                           name=f'path {i}')
              for i, path in enumerate(paths)],
        name=str(k))
        for k in range(len(paths[0]))
    ]

    sliders = base_slider(frames)
    buttons = base_buttons()

    # Layout
    layout = go.Layout(
        scene=dict(
            xaxis=dict(range=[x_range[0], x_range[1]]),
            yaxis=dict(range=[y_range[0], y_range[1]]),
            zaxis=dict(range=[np.min(z), np.max(z)]),
        ),
        updatemenus=buttons,
        sliders=sliders,
    )

    # Create figure
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8, showscale=False)] +
                         [go.Scatter3d(x=path[:, 0], y=path[:, 1], z=[f(x) for x in path],
                                       mode='lines+markers',
                                       name=f'path {i}',
                                       marker=dict(color=i, size=4, symbol='circle',
                                                   line=dict(color='DarkSlateGrey', width=2))) for i, path in
                          enumerate(paths)] +
                         [go.Scatter3d(x=[path[-1, 0]], y=[path[-1, 1]], z=[f(path[-1])],
                                       mode='markers', name=f'end {i}',
                                       marker=dict(color=color_point, size=6, symbol='circle')) for i, path in
                          enumerate(paths)],
                    frames=frames,
                    layout=layout)

    # move play button to the bottom left corner, move slider to the bottom
    # fig.update_layout(updatemenus=[dict(x=0.1, y=-0.7)], sliders=[dict(x=0.2, y=-0.5)])
    # hide the modebar
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0), modebar=dict(bgcolor="rgba(0,0,0,0)"))

    return fig
