import numpy as np
import plotly.graph_objects as go


def plot_figure(paths, f):
    # Create a grid of points
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each point
    z = f([x, y])

    # Define frames
    frames = [go.Frame(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=0.8, showscale=False)] +
                            [go.Scatter3d(x=path[:k + 1, 0], y=path[:k + 1, 1], z=[f(x) for x in path[:k + 1]],
                                          mode='lines+markers', name=f'path {i}') for i, path in enumerate(paths)],
                       name=str(k)) for k in range(len(paths[0]))]

    # Define slider and buttons
    sliders = [{"steps": [{"method": "animate", "args": [[f.name], {"frame": {"duration": 300, "redraw": True},
                                                                    "mode": "immediate",
                                                                    "transition": {"duration": 300}}],
                           "label": str(k)} for k, f in enumerate(frames)],
                "active": 0, "pad": {"b": 10, "t": 60}, "currentvalue": {"prefix": "Step: "}}]

    play_button = [{"type": "buttons", "showactive": False, "buttons": [{"label": "Play",
                                                                         "method": "animate",
                                                                         "args": [None, {
                                                                             "frame": {"duration": 500, "redraw": True},
                                                                             "fromcurrent": True,
                                                                             "transition": {"duration": 300,
                                                                                            "easing": "quadratic-in-out"}}]}]}]

    # Layout
    layout = go.Layout(scene=dict(xaxis=dict(range=[-5, 5]), yaxis=dict(range=[-5, 5]),
                                  zaxis=dict(range=[0, 200])), updatemenus=play_button, sliders=sliders)

    # Create figure
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=0.8, showscale=False)] +
                         [go.Scatter3d(x=path[:, 0], y=path[:, 1], z=[f(x) for x in path],
                                       mode='lines+markers', name=f'path {i}') for i, path in enumerate(paths)],
                    frames=frames, layout=layout)

    return fig
