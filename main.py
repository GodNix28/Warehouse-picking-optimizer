from src.ai_parser import parse_order
from src.visualize import plot_warehouse
from src.warehouse import Warehouse
from src.optimizer import optimize_route, total_distance


warehouse = Warehouse()
entrance = (0, 0)

print("Available products:")
for item in warehouse.products:
    print("-", item)

order = input("\nDescribe your order: ")
items = parse_order(order)

print("\nAI interpreted items:", items)


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

distance = total_distance(route)

print("\nStep-by-step Picking Instructions:")
for i, step in enumerate(route):
    if i == 0:
        print(f"Start at Entrance {step}")
    else:
        print(f"Go to location {step} and pick item")

print(f"\nTotal walking distance: {distance} units")


plot_warehouse(route, warehouse.products)
