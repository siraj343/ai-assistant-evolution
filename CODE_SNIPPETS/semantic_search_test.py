from openai import OpenAI
import os
import numpy
from dotenv import load_dotenv


load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

def get_embedding(text):
    response = client.embeddings.create(
        model = os.getenv("EMBED_MODEL"),
        input = text,
    )
    return response.data[0].embedding

def cosine_similarity(A, B):
    dot_product = numpy.dot(A, B)
    norm_A = numpy.linalg.norm(A)
    norm_B = numpy.linalg.norm(B)
    return dot_product / (norm_A * norm_B)


text1 = "Python is reallly good language for AI and data science"
text2 = "Python is a good programming language"
text3 = "I love eating Apples everyday"


embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)
embedding3 = get_embedding(text3)

similarity_1_2 = cosine_similarity(embedding1, embedding2)
similarity_1_3 = cosine_similarity(embedding1, embedding3)  

print("Similarity between text1 and text2:", f"{similarity_1_2:.2f}")
print("Similarity between text1 and text3:", f"{similarity_1_3:.2f}")