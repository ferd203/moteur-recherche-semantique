# Moteur de Recherche Sémantique avec RAG

Ce projet est un moteur de recherche sémantique développé en Python.
Il permet de charger des documents texte, de les découper en chunks, de générer des embeddings, de les indexer avec FAISS, puis de répondre à une question en utilisant un modèle LLM local via Ollama.

L'objectif principal du projet est de comprendre le fonctionnement interne d'un système RAG sans utiliser directement un framework comme LangChain ou LlamaIndex.

---

## Objectifs du projet

Ce projet permet de comprendre et pratiquer :

- le chargement de documents texte ;
- le découpage de documents en chunks ;
- la génération d'embeddings ;
- la recherche vectorielle avec FAISS ;
- la construction d'un pipeline RAG ;
- l'utilisation d'un LLM local avec Ollama ;
- l'affichage des sources utilisées ;
- la programmation orientée objet en Python ;
- l'utilisation de `@dataclass` ;
- la séparation des responsabilités dans une architecture logicielle.

---


# Technologies utilisées
- Python
- Sentence Transformers
- FAISS
- NumPy
- Ollama
- Llama 3.2 ou autre modèle local
- Dataclasses

## Architecture générale

```text
documents/
    ↓
DocumentLoader
    ↓
list[Chunk]
    ↓
SemanticSearchEngine
    ↓
VectorStore
    ↓
list[SearchResult]
    ↓
RAG
    ↓
PromptBuilder
    ↓
OllamaLLM
    ↓
Réponse + sources


moteur-recherche-semantique/
│
├── app.py
├── chunk.py
├── search_result.py
├── document_loader.py
├── sentence_chunker.py
├── search_engine.py
├── vector_store.py
├── prompt_builder.py
├── rag.py
├── ollama_llm.py
│
├── documents/
│   ├── airflow.txt
│   ├── docker.txt
│   ├── python.txt
│   └── rag.txt
│
├── storage/
│   ├── index.faiss
│   └── chunks.json
│
├── requirements.txt
├── .gitignore
└── README.md