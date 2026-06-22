

from app.knowledge.pinecone_client import index

stats = index.describe_index_stats()

print(stats)