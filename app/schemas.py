from typing import Optional
from datetime import date
from pydantic import BaseModel, Field


class PatientRecord(BaseModel):
    """
    Represents one patient loaded from the dataset.
    """
    patient_id: str
    patient_name: str
    age: int
    gender: str
    diagnosis: str
    current_medication: Optional[str] = None
    lab_test: Optional[str] = None
    lab_value: Optional[float] = None
    lab_unit: Optional[str] = None
    last_visit_date: date
    next_scheduled_visit: Optional[date] = None
    days_since_last_visit: int
    missed_last_appointment: bool
    vitals_bp_systolic: int
    vitals_bp_diastolic: int
    vitals_heart_rate: int
    vitals_spo2: int
    notes: Optional[str] = None


class PatientAnalysis(BaseModel):
    """
    Structured response returned by the LLM.
    """

    risk_level: str = Field(description="Low, Medium or High")
    clinical_summary: str
    follow_up_required: bool
    recommendations: list[str]
    priority_score: int


class AgentState(BaseModel):
    """
    Shared LangGraph state.
    """

    patient_id: int

    patient: Optional[PatientRecord] = None

    analysis: Optional[PatientAnalysis] = None

    report: Optional[str] = None