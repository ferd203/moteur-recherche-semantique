from pathlib import Path

from semantic_rag.document_loader import DocumentLoader
from semantic_rag.sentence_chunker import SentenceChunker
from semantic_rag.search_engine import SemanticSearchEngine
from semantic_rag.prompt_builder import PromptBuilder
from semantic_rag.ollama_llm import OllamaLLM
from semantic_rag.rag import RAG


storage_path = Path("storage")

if storage_path.exists():
    print("Chargement du VectorStore depuis storage...")

    search_engine = SemanticSearchEngine.from_storage(
        directory="storage",
    )

else:
    print("Construction du VectorStore depuis les documents...")

    chunker = SentenceChunker(
        max_sentences=3,
        overlap=1,
    )

    loader = DocumentLoader(
        directory=Path("documents"),
        chunker=chunker,
    )

    chunks = loader.load()

    print(f"Nombre de chunks chargés : {len(chunks)}")

    search_engine = SemanticSearchEngine.from_chunks(
        chunks=chunks,
    )

    search_engine.vector_store.save("storage")


prompt_builder = PromptBuilder()

llm = OllamaLLM(
    model_name="llama3.2",
)

rag = RAG(
    search_engine=search_engine,
    prompt_builder=prompt_builder,
    llm=llm,
)

response = rag.ask(
    question="C'est quoi Python ?",
    top_k=3,
)

print("\nRéponse :")
print(response["answer"])

print("\nSources :")
for result in response["results"]:
    print(
        f"- {result.chunk.source} "
        f"(chunk {result.chunk.chunk_id}) "
        f"distance={result.distance:.4f}"
    )