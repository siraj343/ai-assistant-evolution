from openai import OpenAI
import os
from dotenv import load_dotenv


load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.embeddings.create(
    model = os.getenv("EMBED_MODEL"),
    input = ["I am a good boy", "Python is a good programming language", "He is a good coder"]
)

for i, embedd in enumerate(response.data):
    print(f"embedding {i} length: {len(embedd.embedding)}")  # Print the length of the embedding vector
    print(f"Embedding for input {i}: {embedd.embedding[:5]}...")  # Print first 5 dimensions of the embedding