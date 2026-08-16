from sentence_transformers import SentenceTransformer

from semantic_rag.vector_store import VectorStore


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

store = VectorStore.load(
    "storage"
)

print(
    "Vecteurs rechargés :",
    store.index.ntotal,
)

print(
    "Documents rechargés :",
    len(store.documents),
)

question = (
    "Comment fournir des documents externes "
    "à un modèle de langage ?"
)

query_embedding = model.encode(question)

results = store.search(
    query_embeddings=query_embedding,
    top_k=3,
)

for rank, result in enumerate(
    results,
    start=1,
):
    print(f"\nRésultat {rank}")
    print(result["document"])
    print(
        f"Distance : "
        f"{result['distance']:.4f}"
    )