from pathlib import Path

from .chunk import Chunk
from .sentence_chunker import SentenceChunker


class DocumentLoader:

    def __init__(
        self,
        directory: Path,
        chunker: SentenceChunker,
    ) -> None:
        self.directory = Path(directory)
        self.chunker = chunker

        if not self.directory.exists():
            raise FileNotFoundError(
                f"Le dossier {self.directory} n'existe pas."
            )

        if not self.directory.is_dir():
            raise NotADirectoryError(
                f"{self.directory} n'est pas un dossier."
            )

    def load(self) -> list[Chunk]:
        all_chunks: list[Chunk] = []

        for file_path in self.directory.glob("*.txt"):
            text = file_path.read_text(encoding="utf-8")

            chunks = self.chunker.chunk(text)

            for chunk_id, chunk in enumerate(chunks):
                all_chunks.append(
                    Chunk(
                        document=chunk,
                        source=file_path.name,
                        chunk_id=chunk_id,
                    )
                )

        return all_chunks