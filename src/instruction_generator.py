import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SCALEDOWN_API_KEY")
URL = "https://api.scaledown.xyz/compress/raw/"

def generate_instructions(route):

    route_text = " -> ".join([str(p) for p in route])

    prompt = f"""
You are a warehouse supervisor.

Write clear step-by-step instructions for a worker to follow this picking path:
{route_text}

Make the instructions simple and human friendly.
"""

    payload = {
        "context": "Generate warehouse worker instructions",
        "prompt": prompt,
        "model": "gpt-4o"
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, json=payload)
    data = response.json()

    # We only use the API to optimize the wording
    compressed = data.get("results", {}).get("compressed_prompt", "")

    # Now we generate final instructions locally
    steps = []
    for i, point in enumerate(route):
        if i == 0:
            steps.append(f"Start at the warehouse entrance {point}.")
        else:
            steps.append(f"Walk to shelf location {point} and pick the item.")

    return "\n".join(steps)
