from pathlib import Path

PROMPT_DIR = Path("prompts/patient_analysis.md")

def load_prompt() -> str:
    """ Load prompt template from disk."""
    return PROMPT_DIR.read_text(encoding="utf-8")