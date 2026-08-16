from pathlib import Path

import faiss
import numpy as np
import json

from .chunk import Chunk
from .search_result import SearchResult


class VectorStore:

    def __init__(
        self,
        dimension: int,
    ) -> None:
        self.index = faiss.IndexFlatL2(dimension)
        self.chunks: list[Chunk] = []

    def add(
        self,
        chunks: list[Chunk],
        embeddings: np.ndarray,
    ) -> None:
        if len(chunks) != len(embeddings):
            raise ValueError(
                "Le nombre de chunks doit être égal au nombre d'embeddings."
            )

        self.index.add(embeddings)
        self.chunks.extend(chunks)

    def search(
        self,
        query_embedding: np.ndarray,
        top_k: int = 3,
    ) -> list[SearchResult]:

        distances, indices = self.index.search(
            query_embedding,
            top_k,
        )

        results: list[SearchResult] = []

        for distance, index in zip(distances[0], indices[0]):

            results.append(
                SearchResult(
                    chunk=self.chunks[index],
                    distance=float(distance),
                )
            )

        return results

    def save(
        self,
        directory: str,
    ) -> None:
        out_directory = Path(directory)
        out_directory.mkdir(parents=True, exist_ok=True)

        index_path = out_directory / "index.faiss"
        chunks_path = out_directory / "chunks.json"

        faiss.write_index(
            self.index,
            str(index_path),
        )

        chunks_data = [
            chunk.to_dict()
            for chunk in self.chunks
        ]

        with chunks_path.open(
            mode="w",
            encoding="utf-8",
        ) as file:
            json.dump(
                chunks_data,
                file,
                ensure_ascii=False,
                indent=2
            )

    @classmethod
    def load(
        cls,
        directory: str,
    ) -> "VectorStore":

        out_directory = Path(directory)
        index_path = out_directory / "index.faiss"
        chunks_path = out_directory / "chunks.json"

        if not index_path.exists():
            raise FileNotFoundError(
                f"{chunks_path} doesn't exist."
            )

        if not chunks_path.exists():
            raise FileNotFoundError(
                f"{chunks_path} doesn't exist.")

        index = faiss.read_index(str(index_path))

        with chunks_path.open(
            mode="r",
            encoding="utf-8",
        ) as file:
            chunks_data = json.load(file)

        chunks = [
            Chunk.from_dict(data)
            for data in chunks_data
        ]

        store = cls(
            dimension=index.d
        )

        store.index = index
        store.chunks = chunks

        if store.index.ntotal != len(store.chunks):
            raise ValueError(
                "L'index FAISS et les chunks n'ont pas la même taille"
            )
        return store

