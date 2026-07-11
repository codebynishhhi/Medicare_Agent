from pathlib import Path
from app.llm import llm_gateway
from app.schemas import PatientAnalysis, PatientRecord, AppointmentPlan
from app.utils import prompt_util, template_util
from datetime import timedelta

def analyse_patient(patient):

    prompt = prompt_util.load_prompt()

    final_prompt = f"""
{prompt}

Patient Information:

{patient.model_dump_json(indent=2)}

-----------------------------

Return ONLY valid JSON.

Example format:

{{
    "risk_level": "High",
    "clinical_summary": "...",
    "follow_up_required": true,
    "recommendations": [
        "...",
        "..."
    ],
    "priority_score": 8
}}

Do not return markdown.

Do not explain.

Do not wrap the JSON inside ```json.
Return ONLY the JSON object.
"""

    return llm_gateway.generate_structured(
        final_prompt,
        PatientAnalysis,
    )

def get_appointment_plan(
    patient: PatientRecord,
    analysis: PatientAnalysis,
) -> AppointmentPlan:

    if analysis.priority_score >= 8:
        days = 7
        appointment_type = "Urgent In-Person Consultation"

    elif analysis.priority_score >= 5:
        days = 30
        appointment_type = "Routine Follow-up"

    else:
        days = 90
        appointment_type = "Regular Check-up"

    return AppointmentPlan(
        next_follow_up=patient.last_visit_date + timedelta(days=days),
        appointment_type=appointment_type,
        reason=f"Priority Score: {analysis.priority_score}",
    )

def generate_report(patient:PatientRecord, analysis:PatientAnalysis) -> str:

    # read the template for report generation
    report_template = template_util.get_report_template()
    appointment = get_appointment_plan(patient,analysis,)

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
        priority_score = analysis.priority_score,
        last_visit_date = patient.last_visit_date,
        missed_last_appointment= patient.missed_last_appointment,
        next_follow_up = appointment.next_follow_up,
        appointment_type = appointment.appointment_type,
        reason = appointment.reason
    )
 
    return report


