from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load AI language model (runs locally)
model = SentenceTransformer('all-MiniLM-L6-v2')

WAREHOUSE_ITEMS = [
    "toothpaste",
    "notebook",
    "charger",
    "mouse",
    "keyboard",
    "water bottle"
]

def parse_order(user_text):

    words = user_text.lower().replace(",", "").split()

    found_items = []

    for item in WAREHOUSE_ITEMS:
        similarity = cosine_similarity(
            model.encode([user_text]),
            model.encode([item])
        )[0][0]

        if similarity > 0.35:
            found_items.append(item.replace(" ", "_"))

    return list(set(found_items))
