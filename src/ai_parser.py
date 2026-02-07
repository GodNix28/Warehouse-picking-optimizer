import os
from dotenv import load_dotenv
from openai import OpenAI

# Load .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("SCALEDOWN_API_KEY"),
    base_url=os.getenv("SCALEDOWN_BASE_URL")
)

def parse_order(user_text):

    system_prompt = """
You are a warehouse assistant.

From the user's sentence, extract only the product names that exist in the warehouse.

Return ONLY a comma-separated list.

Available products:
toothpaste, notebook, charger, mouse, keyboard, water_bottle
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_text}
        ],
        temperature=0
    )

    items_text = response.choices[0].message.content.strip()

    return [i.strip() for i in items_text.split(",")]
