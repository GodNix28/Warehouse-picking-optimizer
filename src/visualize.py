import matplotlib.pyplot as plt

def plot_warehouse(route, products):
    fig, ax = plt.subplots(figsize=(7,7))

    # Plot shelves
    for item, (x, y) in products.items():
        ax.scatter(x, y, s=120)
        ax.text(x+0.1, y+0.1, item, fontsize=9)

    # Entrance
    ax.scatter(0, 0, s=250, marker="s")
    ax.text(0.1, 0.1, "Entrance", fontsize=10)

    # Route path
    if route and len(route) > 1:
        xs = [p[0] for p in route]
        ys = [p[1] for p in route]
        ax.plot(xs, ys, linewidth=3)

    ax.set_title("Optimized Picking Path")
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 10)
    ax.grid(True)

    return fig
