class Warehouse:
    def __init__(self):
        # Grid size (10x10 warehouse)
        self.width = 10
        self.height = 10
        
        # Product locations (x, y coordinates)
        self.products = {
            "toothpaste": (2, 8),
            "notebook": (5, 1),
            "charger": (9, 6),
            "mouse": (3, 4),
            "keyboard": (7, 2),
            "water_bottle": (1, 5)
        }

    def get_location(self, item):
        return self.products.get(item, None)
