from src.visualize import plot_warehouse
from src.warehouse import Warehouse
from src.optimizer import optimize_route

warehouse = Warehouse()
entrance = (0, 0)

print("Available products:")
for item in warehouse.products:
    print("-", item)

order = input("\nEnter items separated by comma: ")
items = [i.strip() for i in order.split(",")]

locations = []

for item in items:
    loc = warehouse.get_location(item)
    if loc:
        locations.append(loc)
    else:
        print(f"{item} not found in warehouse")

route = optimize_route(entrance, locations)

print("\nOptimized Picking Route:")
for step in route:
    print(step)

plot_warehouse(route, warehouse.products)
