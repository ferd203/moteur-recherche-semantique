from ollama import Client, ResponseError


class OllamaLLM:
    def __init__(
        self,
        model_name: str = "qwen3:4b",
        host: str = "http://localhost:11434",
    ) -> None:
        self.model_name = model_name
        self.client = Client(host=host)

    def generate(self, prompt: str) -> str:
        if not prompt.strip():
            raise ValueError(
                "Le prompt ne peut pas être vide."
            )

        try:
            response = self.client.generate(
                model=self.model_name,
                prompt=prompt,
                stream=False,
            )

        except ResponseError as error:
            raise RuntimeError(
                f"Erreur retournée par Ollama : {error}"
            ) from error

        except ConnectionError as error:
            raise RuntimeError(
                "Impossible de contacter Ollama. "
                "Vérifie que le service est démarré."
            ) from error

        return response.response.strip()