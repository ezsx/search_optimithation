import numpy as np
import plotly.graph_objects as go


def plot_figure2(paths, f):
    # Create a grid of points
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each point
    z = f([x, y])

    # Define frames
    frames = [go.Frame(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=0.8, showscale=False)] +
                            [go.Scatter3d(x=path[:k + 1, 0], y=path[:k + 1, 1], z=[f(x) for x in path[:k + 1]],
                                          mode='lines+markers', name=f'path {i}',
                                          marker=dict(color=i, size=6, symbol='circle',
                                                      line=dict(color='DarkSlateGrey', width=2))) for i, path in
                             enumerate(paths)],
                       name=str(k)) for k in range(len(paths[0]))]

    # Define slider and buttons
    sliders = [{"steps": [{"method": "animate", "args": [[f.name], {"frame": {"duration": 300, "redraw": True},
                                                                    "mode": "immediate",
                                                                    "transition": {"duration": 300}}],
                           "label": str(k)} for k, f in enumerate(frames)],
                "active": 0, "pad": {"b": 10, "t": 60}, "currentvalue": {"prefix": "Step: "}}]

    play_button = [{"type": "buttons", "showactive": False, "buttons": [{"label": "▶",
                                                                         "method": "animate",
                                                                         "args": [None, {
                                                                             "frame": {"duration": 500, "redraw": True},
                                                                             "fromcurrent": True,
                                                                             "transition": {"duration": 300,
                                                                                            "easing": "quadratic-in-out"}}]}]}]

    play_button_color_style = {"bgcolor": "rgba(0,0,0,0)", "bordercolor": "rgba(0,0,0,0)"}
    play_button[0]["buttons"][0]["args"][1].update(play_button_color_style)

    # Layout
    layout = go.Layout(title='Optimization Paths',
                       scene=dict(xaxis=dict(title='X', range=[-5, 5]),
                                  yaxis=dict(title='Y', range=[-5, 5]),
                                  zaxis=dict(title='Z', range=[-200, 1200])),
                       updatemenus=play_button, sliders=sliders)

    # Create figure
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale='Viridis', opacity=0.8, showscale=False)] +
                         [go.Scatter3d(x=path[:, 0], y=path[:, 1], z=[f(x) for x in path],
                                       mode='lines+markers', name=f'path {i}',
                                       marker=dict(color=i, size=6, symbol='circle',
                                                   line=dict(color='DarkSlateGrey', width=2))) for i, path in
                          enumerate(paths)],
                    frames=frames, layout=layout)

    # add new color to surface
    surface_color = np.zeros((100, 100))
    surface_color[0, 0] = 1
    fig.data[0].surfacecolor = surface_color
    fig.data[0].colorbar = dict(thickness=20, ticklen=4)

    # move play button to the bottom left corner
    fig.update_layout(updatemenus=[dict(x=-0.1, y=-0.5)])

    return fig
