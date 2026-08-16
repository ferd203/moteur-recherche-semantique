import re


class SentenceChunker:

    def __init__(
        self,
        max_sentences: int = 3,
        overlap: int = 1,
    ) -> None:
        self.max_sentences = max_sentences
        self.overlap = overlap

        if overlap >= max_sentences:
            raise ValueError(
                "overlap doit être inférieur à max_sentences."
            )

    def split_sentences(
        self,
        text: str,
    ) -> list[str]:

        sentences = re.split(
            r"(?<=[.!?])\s+",
            text.strip(),
        )

        return [
            sentence.strip()
            for sentence in sentences
            if sentence.strip()
        ]

    def chunk(
        self,
        text: str,
    ) -> list[str]:

        sentences = self.split_sentences(text)

        chunks: list[str] = []

        step = self.max_sentences - self.overlap

        for start in range(0, len(sentences), step):
            end = start + self.max_sentences

            chunk = " ".join(
                sentences[start:end]
            )

            if chunk.strip():
                chunks.append(chunk)

        return chunks