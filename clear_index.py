# clear_index.py

from app.knowledge.pinecone_client import index

index.delete(
    delete_all=True,
    namespace="support-docs"
)

print("✅ Namespace cleared")