# test_chunking.py

from pathlib import Path
from app.knowledge.chunker import chunk_text

content = Path(
    "docs/test_large_doc.txt"
).read_text()

chunks = chunk_text(content)

print(f"Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks):
    print("\n")
    print("=" * 50)
    print(f"Chunk {i}")
    print(chunk)