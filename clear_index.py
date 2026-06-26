# clear_index.py

from app.knowledge.pinecone_client import index

from app.config import PINECONE_NAMESPACE

index.delete(
    delete_all=True,
    namespace=PINECONE_NAMESPACE
)

print("✅ Namespace cleared")