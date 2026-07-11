from langchain_litellm import ChatLiteLLM

from app.config import settings
from app.schemas import PatientAnalysis


class LLMGateway:
    """
    Centralized LLM Gateway.

    The rest of the application should never know
    whether we are using Groq, OpenAI, Gemini or Claude.
    """

    def __init__(self):

        self.llm = ChatLiteLLM(

            model=settings.model_name,

            api_key=settings.groq_api_key,

            temperature=settings.temperature,
        )

    def analysis_model(self):

        return self.llm.with_structured_output(
            PatientAnalysis
        )


llm_gateway = LLMGateway()