# gemini_api.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
ENDPOINT = "https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

def call_gemini(prompt: str, max_tokens=64, temperature=0.7):
    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "temperature": temperature,
            "maxOutputTokens": max_tokens
        }
    }

    try:
        response = requests.post(
            f"{ENDPOINT}?key={API_KEY}",
            headers=headers,
            json=payload
        )
        if response.status_code == 200:
            result = response.json()
            return result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "N/A").strip()
        else:
            print(f"❌ Gemini API error {response.status_code}: {response.text}")
            return "N/A"
    except Exception as e:
        print(f"❌ Gemini API exception: {e}")
        return "N/A"
