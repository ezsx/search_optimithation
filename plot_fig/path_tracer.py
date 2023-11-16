import numpy as np
import plotly.graph_objects as go


def plot_traces(paths, f, color_scale='rdbu'):
    # Create a grid of points
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)

    # Compute the function value at each point
    z = f([x, y])

    # Define frames
    frames = [go.Frame(
        data=[go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8, showscale=False)] +

             [go.Scatter3d(x=path[:k + 1, 0],
                           y=path[:k + 1, 1],
                           z=[f(x) for x in path[:k + 1]],
                           mode='lines+markers',
                           name=f'path {i}')
              for i, path in enumerate(paths)],
        name=str(k))
        for k in range(len(paths[0]))
    ]

    # Define slider and buttons
    # Define slider and buttons
    sliders = [
        {
            "steps": [
                {
                    "method": "animate",
                    "args": [
                        [f.name],
                        {
                            "frame": {"duration": 300, "redraw": True},
                            "mode": "immediate",
                            "transition": {"duration": 300}
                        }
                    ],
                    "label": str(k)
                } for k, f in enumerate(frames)
            ],
            "active": 0,
            "currentvalue": {"prefix": "Step: "},
            "transition": {"duration": 300, "easing": "cubic-in-out"},  # Customize the transition
            "x": 0.1,  # Adjust the x position of the slider
            "len": 0.9,  # Adjust the length of the slider
            "xanchor": "left",  # Anchor the x position of the slider to the left
            "y": 0,  # Adjust the y position of the slider
            "yanchor": "top",  # Anchor the y position of the slider to the top
            "currentvalue_font": {"size": 20, "color": "#000000"},  # Customize the font for the current value
            "font": {"size": 12, "color": "#666666"},  # Customize the font for the slider
            "borderwidth": 2,  # Add border width to the slider
            "bordercolor": "#666666",  # Set the border color of the slider
            "bgcolor": "#f9f9f9",  # Set the background color of the slider
        }
    ]

    # style slider
    # slider_style = {"bgcolor": "black", "bordercolor": "black", "font": {"color": "black"}}
    # sliders[0].update(slider_style)

    buttons = [{"type": "buttons",
                "showactive": False,
                "buttons": [{"label": "▶",
                             "method": "animate",
                             "args": [None, {
                                 "frame": {"duration": 200, "redraw": True},
                                 "fromcurrent": True,
                                 "transition": {"duration": 100,
                                                "easing": "quadratic-in-out"}}]}
                    , {"label": "❚❚",
                       "method": "animate",
                       "args": [[None], {"frame": {"duration": 0, "redraw": True},
                                         "mode": "immediate",
                                         "transition": {"duration": 0}}],

                       }]}]

    # Style the play button
    play_button_color_style = {"bgcolor": "rgba(0,0,0,0)", "bordercolor": "rgba(0,0,0,0)"}
    buttons[0]["buttons"][0]["args"][1].update(play_button_color_style)

    # Layout
    layout = go.Layout(scene=dict(xaxis=dict(range=[-5, 5]), yaxis=dict(range=[-5, 5]),
                                  zaxis=dict(range=[-200, 1000])), updatemenus=buttons, sliders=sliders)

    # Create figure
    fig = go.Figure(data=[go.Surface(x=x, y=y, z=z, colorscale=color_scale, opacity=0.8, showscale=False)] +
                         [go.Scatter3d(x=path[:, 0], y=path[:, 1], z=[f(x) for x in path],
                                       mode='lines+markers', name=f'path {i}',
                                       marker=dict(color=i, size=4, symbol='circle',
                                                   line=dict(color='DarkSlateGrey', width=2))) for i, path in
                          enumerate(paths)] +
                         [go.Scatter3d(x=[path[-1, 0]], y=[path[-1, 1]], z=[f(path[-1])],
                                       mode='markers', name=f'end {i}',
                                       marker=dict(color='gold', size=6, symbol='circle')) for i, path in
                          enumerate(paths)],
                    frames=frames, layout=layout)

    # move play button to the bottom left corner, move slider to the bottom
    # fig.update_layout(updatemenus=[dict(x=0.1, y=-0.7)], sliders=[dict(x=0.2, y=-0.5)])
    fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
    # hide the modebar
    fig.update_layout(modebar=dict(bgcolor="rgba(0,0,0,0)"))

    return fig