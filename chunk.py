from dataclasses import dataclass


@dataclass
class Chunk:
    document: str
    source: str
    chunk_id: int

    def to_dict(self) -> dict:
        return {
            "document": self.document,
            "source": self.source,
            "chunk_id": self.chunk_id,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Chunk":
        return cls(
            document=data["document"],
            source=data["source"],
            chunk_id=data["chunk_id"],
        )