from pathlib import Path
from app.schemas import AgentState

TEMPLATE_DIR = Path("templates/patient_report.md")

def get_report_template() -> str:
    """ Return the template for the report generation"""
    return TEMPLATE_DIR.read_text(encoding="utf-8")