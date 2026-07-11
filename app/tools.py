from pathlib import Path
from app.llm import llm_client
from app.schemas import PatientAnalysis, PatientRecord
from app.utils import prompt_util, template_util


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

def generate_report(patient:PatientRecord, analysis:PatientAnalysis) -> str:
    # read the template for report generation
    report_template = template_util.get_report_template()
    report = report_template.format(
        patient_id = patient.patient_id,
        patient_name = patient.patient_name,
        age = patient.age,
        gender = patient.gender,
        diagnosis = patient.diagnosis,
        current_medication = patient.current_medication,
        risk_level = analysis.risk_level,
        clinical_summary = analysis.clinical_summary,
        recommendations = "\n".join(f"- {item}" for item in analysis.recommendations),
        follow_up_required = analysis.follow_up_required,
        priority_score = analysis.priority_score
    )
 
    return report
