import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()
groq_api_key=os.getenv("GROQ_API_KEY")
client = Groq(api_key=groq_api_key)

SYSTEM_PROMPT = """
You are an AI assistant helping a building materials company classify website inquiries.

Classify the inquiry into exactly ONE of the following categories:
- Hot Lead
- Medium Lead
- Low Lead
- Support

Definitions:
Hot Lead: High intent sales inquiry asking about pricing, timelines, bulk orders, or active projects.
Medium Lead: General product interest, catalog requests, or early-stage inquiries.
Low Lead: Browsing or informational questions with no buying intent.
Support: Existing customer support issues, complaints, or order-related problems.

Respond with ONLY the category name.
"""

def classify_lead(message: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant", # have to try other model. maybe better to go something small.
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": message}
        ],
        temperature=0
    )

    category = response.choices[0].message.content.strip()

    if category not in ["Hot Lead", "Medium Lead", "Low Lead", "Support"]:
        category = "Medium Lead"

    return {
        "category": category,
        "confidence": 1.0
    }
