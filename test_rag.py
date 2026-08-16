from document_loader import DocumentLoader
from ollama_llm import OllamaLLM
from prompt_builder import PromptBuilder
from rag import RAG
from search_engine import SemanticSearchEngine
from sentence_chunker import SentenceChunker


# 1. Créer le chunker
chunker = SentenceChunker(
    max_sentences=3,
    overlap=1,
)

# 2. Charger les documents
loader = DocumentLoader(
    directory="documents",
    chunker=chunker,
)

documents = loader.load()

print(f"{len(documents)} chunks chargés.")

# 3. Créer le moteur de recherche
search_engine = SemanticSearchEngine(chunks=documents, storage_directory="storage")

# 4. Créer le constructeur de prompt
prompt_builder = PromptBuilder()

# 5. Créer le client LLM
llm = OllamaLLM(
    model_name="qwen3:4b",
)

# 6. Injecter les dépendances dans RAG
rag = RAG(
    search_engine=search_engine,
    prompt_builder=prompt_builder,
    llm=llm,
)

# 7. Poser une question
question = input("\nPose ta question : ")

response = rag.ask(
    question=question,
    top_k=3,
)

# 8. Afficher la réponse
print("\n================ RÉPONSE ================\n")
print(response["answer"])

# 9. Afficher les sources
print("\n================ SOURCES ================\n")

for rank, source in enumerate(
    response["sources"],
    start=1,
):
    print(f"Source {rank}")
    print(source["document"])
    print(f"Distance : {source['distance']:.4f}")
    print("-" * 50)