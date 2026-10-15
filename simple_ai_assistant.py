from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()   # by default looks for .env file

client = OpenAI(
    base_url = os.getenv("BASE_URL"),
    api_key =os.getenv("API_KEY")
)

while True:

    user_input = input("\nSiraj: ")

    if user_input.lower in ["exit", "quit", "bye", "byeee", "goodboy"]:
        break

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages = [
            {
                "role":"user",
                "content":"Hello LLM!"
            }
        ]
    )
    print("Assistant: " + response.choices[0].message.content) # Response from the LLM
    print(response.choices[0].message.role)

