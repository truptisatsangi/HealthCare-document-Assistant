from langchain.chat_models import init_chat_model

class LLMService:
    """
    Responsible for interacting with the Large Language Model.

    Responsibilities:
    - Initialize the LLM.
    - Send the final prompt.
    - Return the generated response.
    """

    def __init__(self):
        self.llm = init_chat_model(
            "microsoft/Phi-3-mini-4k-instruct",
            model_provider="huggingface",
            temperature=0.2,
            max_tokens=1024,
        )

    def generate_response(self, prompt: str) -> str:
        response = self.llm.invoke(prompt)

        return response.content