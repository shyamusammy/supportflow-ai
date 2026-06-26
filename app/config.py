import os
from dotenv import load_dotenv

load_dotenv()

# Environment Variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_INDEX = os.getenv("PINECONE_INDEX")

# Pinecone
PINECONE_NAMESPACE = "support-docs"

# Retrieval
TOP_K = 5
MIN_SCORE = 0.65

# Embeddings
EMBEDDING_MODEL = "gemini-embedding-001"

# Chunking
CHUNK_SIZE = 200
CHUNK_OVERLAP = 50