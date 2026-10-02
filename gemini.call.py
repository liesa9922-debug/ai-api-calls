import os
import google.generativeai as genai

# Retrieve API key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise ValueError("GEMINI_API_KEY is not set.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-flash-latest")

prompt = "Explain the CIA Triad in cybersecurity in two sentences."
response = model.generate_content(prompt)

print("=== Gemini API Response ===")
print(response.text)
