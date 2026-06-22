from app.knowledge.retrieval import retrieve_documents

results = retrieve_documents(
    query="Best restaurants in Paris",
    department="login"
)

if not results:
    print("\n❌ No relevant documents found")
else:
    for doc in results:
        print("\n" + "=" * 50)
        print("Source:", doc["source"])
        print("Score:", doc["score"])
        print(doc["content"])