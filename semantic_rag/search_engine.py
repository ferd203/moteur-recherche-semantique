from sentence_transformers import SentenceTransformer

from .chunk import Chunk
from .search_result import SearchResult
from .vector_store import VectorStore


class SemanticSearchEngine:

    def __init__(
        self,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> None:
        self.model = SentenceTransformer(model_name)
        self.vector_store: VectorStore | None = None

    @classmethod
    def from_chunks(
        cls,
        chunks: list[Chunk],
        model_name: str = "all-MiniLM-L6-v2",
    ) -> "SemanticSearchEngine":

        if not chunks:
            raise ValueError(
                "Aucun chunk reçu. Impossible de construire le moteur de recherche."
            )

        engine = cls(
            model_name=model_name,
        )

        texts = [
            chunk.document
            for chunk in chunks
        ]

        embeddings = engine.model.encode(texts)

        vector_store = VectorStore(
            dimension=embeddings.shape[1],
        )

        vector_store.add(
            chunks=chunks,
            embeddings=embeddings,
        )

        engine.vector_store = vector_store

        return engine

    @classmethod
    def from_storage(
        cls,
        directory: str,
        model_name: str = "all-MiniLM-L6-v2",
    ) -> "SemanticSearchEngine":

        engine = cls(
            model_name=model_name,
        )

        engine.vector_store = VectorStore.load(
            directory=directory,
        )

        return engine

    def search(
        self,
        question: str,
        top_k: int = 3,
    ) -> list[SearchResult]:

        if self.vector_store is None:
            raise ValueError(
                "VectorStore non initialisé. Utilise from_chunks() ou from_storage()."
            )

        query_embedding = self.model.encode(
            [question]
        )

        return self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )