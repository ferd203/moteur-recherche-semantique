from ollama_llm import OllamaLLM
from search_engine import SemanticSearchEngine
from prompt_builder import PromptBuilder

class RAG:
    def __init__(
            self,
            search_engine : SemanticSearchEngine,
            prompt_builder : PromptBuilder,
            llm : OllamaLLM,
    )->None:
        self.search_engine = search_engine
        self.prompt_builder = prompt_builder
        self.llm = llm

    def ask(
            self,
            question: str,
            top_k: int = 3,
    ) -> dict[str, str | list[dict[str, str | float]]]:
        if not question.strip():
            raise ValueError(
                "La question ne peut pas être vide."
            )

        results = self.search_engine.search(
            question=question,
            top_k=top_k,
        )

        chunks = [
            result.chunk
            for result in results
        ]
        prompt = self.prompt_builder.build(
            question=question,
            chunks=chunks,
        )

        answer = self.llm.generate(prompt)

        return {
            "question": question,
            "answer": answer,
            "results": results,
        }