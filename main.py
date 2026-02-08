from src.instruction_generator import generate_instructions
from src.orders import read_order, process_order
from src.visualize import plot_warehouse
from src.warehouse import Warehouse
from src.optimizer import optimize_route, total_distance


warehouse = Warehouse()
entrance = (0, 0)

print("Available products:")
for item in warehouse.products:
    print("-", item)

# --- Read and process order (handled by orders.py) ---
order_text = read_order()
urgent_items, normal_items = process_order(order_text)

items = urgent_items + normal_items

print("\nUrgent items:", urgent_items)
print("Normal items:", normal_items)
print("\nAI interpreted items:", items)

# --- Get locations ---
locations = []
for item in items:
    loc = warehouse.get_location(item)
    if loc:
        locations.append(loc)
    else:
        print(f"{item} not found in warehouse")

# Separate locations
urgent_locations = [warehouse.get_location(i) for i in urgent_items if warehouse.get_location(i)]
normal_locations = [warehouse.get_location(i) for i in normal_items if warehouse.get_location(i)]

# --- Route optimization ---
route = [entrance]

# Optimize urgent first
if urgent_locations:
    urgent_route = optimize_route(route[-1], urgent_locations)
    route += urgent_route[1:]

# Then normal items
if normal_locations:
    normal_route = optimize_route(route[-1], normal_locations)
    route += normal_route[1:]

# --- Display route ---
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

# --- AI Instructions ---
print("\nAI Generated Worker Instructions:")
print(generate_instructions(route))

# --- Visualization ---
plot_warehouse(route, warehouse.products)
