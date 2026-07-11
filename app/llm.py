from langchain_groq import ChatGroq
from app.schemas import PatientAnalysis
from app.config import settings

class LLMClient:
    def __init__(self):
        self.llm = ChatGroq(
            model = settings.model_name,
            api_key = settings.groq_api_key,
            temperature=settings.temperature
        )
    
    def analysis_model(self):
        return self.llm.with_structured_output(PatientAnalysis)
    
llm_client = LLMClient()