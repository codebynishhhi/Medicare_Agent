from app.repository import RepositoryLoader as PatientLoader
from app.tools import analyse_patient
from app.schemas import AgentState

# load the patient 
loader = PatientLoader()

# Node 1 - Load the patient
def load_patient_node(state: AgentState):
    # load patient using id
    patient = loader.get_patient(state.patient_id)
    state.patient = patient
    return state

# Node 2 - Analyse the patient 
def analyse_patient_node(state:AgentState):
    analysis = analyse_patient(state.patient)
    state.analysis = analysis
    return analysis