import os

from dotenv import load_dotenv
from google import genai

from app.config import EMBEDDING_MODEL
from app.logger import logger

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

logger.info(
    f"Google API Key Loaded: "
    f"{bool(api_key)}"
)

client = genai.Client(
    api_key=api_key
)


def create_embedding(text: str):

    response = client.models.embed_content(
        model=EMBEDDING_MODEL,
        contents=text
    )

    return response.embeddings[0].values