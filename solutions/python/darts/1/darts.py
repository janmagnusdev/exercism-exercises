"""
Score computation for darting game.
"""

def is_inside_circle(px, py, cx, cy, r):
    dx = px - cx
    dy = py - cy
    return dx*dx + dy*dy <= r*r


def score(x, y):
    """
    x: x position of hit
    y: y position of hit

    0,0 is middle point of target
    -1 to 1 is inner circle
    -5 to 5 is middle circle
    -10 to 10 is outer circle
    everything else is miss
    """
    radius_bounds = {
        (1): 10,
        (5): 5,
        (10): 1
    }

    for (r), points in radius_bounds.items():
        if is_inside_circle(x, y, 0, 0, r):
            return points
    return 0
