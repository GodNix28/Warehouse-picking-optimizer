from src.warehouse import Warehouse

warehouse = Warehouse()

print("Available products:")
for item in warehouse.products:
    print(item)

item = input("\nEnter item name: ")

location = warehouse.get_location(item)

if location:
    print(f"{item} is located at position {location}")
else:
    print("Item not found")
