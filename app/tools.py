from pathlib import Path
from app.llm import llm_client
from app.schemas import PatientAnalysis, PatientRecord
from app.utils import prompt_util


def analyse_patient(patient:PatientRecord) -> PatientAnalysis:
    """
    Tool 1 : Analyse a patient's condition using the LLM.
    """
    prompt = prompt_util.load_prompt()
    final_prompt = f""" 
            {prompt} 
            Patient Information
            {patient.model_dump_json(indent=2)}
    """
    structure_llm = llm_client.analysis_model()
    response = structure_llm.invoke(final_prompt)
    return response