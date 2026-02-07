import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("SCALEDOWN_API_KEY")

URL = "https://api.scaledown.xyz/v1/responses"

def parse_order(user_text):

    system_prompt = """
Extract the product names from the sentence.

Return ONLY a comma separated list using these allowed items:
toothpaste, notebook, charger, mouse, keyboard, water_bottle
"""

    payload = {
        "model": "gpt-4o",
        "input": f"{system_prompt}\n\nSentence: {user_text}"
    }

    headers = {
        "x-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    response = requests.post(URL, headers=headers, json=payload)

    data = response.json()

    print("\nFULL API RESPONSE:")
    print(data)

    try:
        content = data["output"][0]["content"][0]["text"]
    except:
        return []

    return [i.strip() for i in content.split(",")]
