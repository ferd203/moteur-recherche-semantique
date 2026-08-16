from .chunk import Chunk



class PromptBuilder:

    def build(
        self,
        question: str,
        chunks: list[Chunk],
    ) -> str:

        prompt = """
Tu es un assistant intelligent.

Réponds à la question en utilisant uniquement le contexte fourni.
Si le contexte ne contient pas la réponse, dis clairement que tu ne sais pas.


==========================================================================
CONTEXTE
==========================================================================
"""

        for indice, chunk in enumerate(chunks, start=1):

            prompt += f"""
[{indice}]
{chunk.document}

"""

        prompt += f"""
==================================================================
QUESTION
===================================================================
{question}
===================================================================
REPONSE
===================================================================
"""

        return prompt