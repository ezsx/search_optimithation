def base_slider(frames):
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
    return sliders


def base_buttons():
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
    # play_button_color_style = {"bgcolor": "rgba(0,0,0,0)", "bordercolor": "rgba(0,0,0,0)"}
    # buttons[0]["buttons"][0]["args"][1].update(play_button_color_style)

    return buttons

