from src.ai_parser import parse_order

def read_order():
    """
    Reads multi-line order input from the user.
    User types DONE to finish.
    """

    print("\nDescribe your order (type DONE on a new line when finished):")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == "DONE":
            break
        lines.append(line)

    return "\n".join(lines)


def process_order(order_text):
    """
    Separates urgent and normal items and interprets them.
    """

    urgent_items = []
    normal_items = []

    for line in order_text.split("\n"):
        if "urgent" in line.lower():
            urgent_items += parse_order(line)
        else:
            normal_items += parse_order(line)

    # remove duplicates
    urgent_items = list(dict.fromkeys(urgent_items))
    normal_items = [i for i in normal_items if i not in urgent_items]

    return urgent_items, normal_items
