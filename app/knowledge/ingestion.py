from pathlib import Path

from app.knowledge.embedder import create_embedding
from app.knowledge.pinecone_client import index
from app.knowledge.chunker import chunk_text

DOCS_PATH = "docs"


def ingest_documents():

    for file in Path(DOCS_PATH).glob("*.txt"):

        print(f"Processing: {file.name}")

        content = file.read_text(
            encoding="utf-8"
        )

        chunks = chunk_text(content)

        print(f"Total Chunks: {len(chunks)}")

        for i, chunk in enumerate(chunks):

            embedding = create_embedding(chunk)

            vector_id = f"{file.stem}_chunk_{i}"

            department = file.stem.split("_")[0]

            print(f"Department: {department}")

            index.upsert(
                vectors=[
                    {
                        "id": vector_id,
                        "values": embedding,
                        "metadata": {
                            "source": file.name,
                            "chunk_id": i,
                            "content": chunk,
                            "department": department,
                            "document_type": "policy"
                        }
                    }
                ],
                namespace="support-docs"
            )

            print(f"✅ Ingested {vector_id}")


if __name__ == "__main__":
    ingest_documents()