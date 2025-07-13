import os
from dotenv import load_dotenv
import requests


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")


def ask_llm(prompt: str, model="llama3-8b-8192") -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful code assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.2,
        "max_tokens": 512
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()  
    result = response.json()
    return result["choices"][0]["message"]["content"].strip()