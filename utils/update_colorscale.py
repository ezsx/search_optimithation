# Function to update the colorscale
def update_colorscale(fig, new_color_scale):
    """
    Update the colorscale of a plotly figure

    :parameter
    ----------
    fig (plotly.graph_objects.Figure): The figure to update.
    new_color_scale (str): The new colorscale to use.

    :return
    -------
    plotly.graph_objects.Figure: The updated figure.
    """
    for trace in fig['data']:
        if 'type' in trace and trace['type'] == 'surface':
            trace['colorscale'] = new_color_scale
    return fig
