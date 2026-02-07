import matplotlib.pyplot as plt

def plot_warehouse(route, products):
    plt.figure(figsize=(6,6))

    # Plot all product locations
    for item, loc in products.items():
        plt.scatter(loc[0], loc[1])
        plt.text(loc[0]+0.1, loc[1]+0.1, item, fontsize=8)

    # Plot the path
    x = [point[0] for point in route]
    y = [point[1] for point in route]
    plt.plot(x, y, marker='o')

    # Entrance
    plt.scatter(route[0][0], route[0][1], s=100, marker='s')
    plt.text(route[0][0]+0.1, route[0][1]+0.1, "Entrance", fontsize=9)

    plt.title("Optimized Warehouse Picking Route")
    plt.xlim(0,10)
    plt.ylim(0,10)
    plt.grid(True)

    plt.show()
