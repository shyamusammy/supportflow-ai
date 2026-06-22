import os

from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX")

print("Pinecone API Key Loaded:", api_key is not None)
print("Pinecone Index:", index_name)

pc = Pinecone(
    api_key=api_key
)

index = pc.Index(index_name)