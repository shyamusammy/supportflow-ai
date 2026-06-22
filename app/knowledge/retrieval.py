from app.knowledge.embedder import create_embedding
from app.knowledge.pinecone_client import index

MIN_SCORE = 0.65


def retrieve_documents(
    query: str,
    department: str | None = None,
    top_k: int = 5
):

    query_embedding = create_embedding(query)

    query_params = {
        "namespace": "support-docs",
        "vector": query_embedding,
        "top_k": top_k,
        "include_metadata": True,
    }

    if department:
        query_params["filter"] = {
            "department": department
        }

    results = index.query(**query_params)

    documents = []

    for match in results.get("matches", []):

        score = match["score"]

        print(
            f"Score: {score:.4f} | "
            f"Source: {match['metadata']['source']}"
        )

        if score < MIN_SCORE:
            continue

        documents.append(
            {
                "score": score,
                "source": match["metadata"]["source"],
                "content": match["metadata"]["content"]
            }
        )

    return documents