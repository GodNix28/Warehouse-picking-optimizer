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


def total_distance(route):
    """Calculate total walking distance of the route"""
    dist = 0
    for i in range(len(route) - 1):
        dist += manhattan_distance(route[i], route[i+1])
    return dist

def naive_route(start, locations):
    """
    Simulates a worker walking in the given order without optimization.
    """
    route = [start]
    for loc in locations:
        route.append(loc)
    return route
