def manhattan_distance(p1, p2):
    """
    Calculates walking distance in a warehouse grid.
    Workers cannot move diagonally.
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def optimize_route(start, locations):
    """
    Nearest Neighbor Optimization.
    Always go to the closest next item.
    """

    remaining = locations.copy()
    route = [start]
    current = start

    while remaining:
        nearest = min(remaining, key=lambda point: manhattan_distance(current, point))
        route.append(nearest)
        remaining.remove(nearest)
        current = nearest

    return route
