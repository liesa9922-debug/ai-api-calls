import os
from openai import OpenAI

# Retrieve API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set.")

client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a concise technical tutor."},
        {"role": "user", "content": "Explain the CIA Triad in cybersecurity in two sentences."}
    ]
)

print("=== OpenAI API Response ===")
print(response.choices[0].message.content)
