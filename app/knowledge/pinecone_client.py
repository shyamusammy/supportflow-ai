import os

from dotenv import load_dotenv
from pinecone import Pinecone

from app.logger import logger

load_dotenv()

api_key = os.getenv("PINECONE_API_KEY")
index_name = os.getenv("PINECONE_INDEX")

logger.info(
    f"Pinecone API Key Loaded: "
    f"{bool(api_key)}"
)

logger.info(
    f"Pinecone Index: {index_name}"
)

pc = Pinecone(
    api_key=api_key
)

index = pc.Index(index_name)