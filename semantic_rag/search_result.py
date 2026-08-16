from dataclasses import dataclass


from .chunk import Chunk



@dataclass
class SearchResult:
    chunk : Chunk
    distance : float