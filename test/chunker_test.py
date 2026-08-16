from sentence_chunker import SentenceChunker
from document_loader import DocumentLoader
from pathlib import Path

chunker = SentenceChunker(
    max_sentences=3,
    overlap=1
)

path = Path(__file__).resolve().parent.parent

doc = DocumentLoader(directory= path/"documents", chunker=chunker)
chunks = doc.load()
print(f"Chunks: {len(chunks)}")

for index, chunk in enumerate(chunks, start=1):
    print(f"\nChunk {index}")
    print(chunk)