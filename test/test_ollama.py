from ollama_llm import OllamaLLM


llm = OllamaLLM(
    model_name="qwen3:4b",
)

response = llm.generate(
    "Explique le RAG en trois phrases simples."
)

print(response)