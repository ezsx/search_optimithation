def rez_output(initial_points, founded_minimum, function):
    s = f"start point [X:{initial_points[0]:.2f}, Y:{initial_points[1]:.2f}, Z:{function(initial_points):.2f}]" \
        f" founded minimum [X:{founded_minimum[0]:.2f}, Y:{founded_minimum[1]:.2f}, Z:{function(founded_minimum):.2f}]" + "\n"
    return s


def format_output(output):
    return ' \n'.join(output)
