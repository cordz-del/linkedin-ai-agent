import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_ai_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]
