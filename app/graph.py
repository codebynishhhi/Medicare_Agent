from langgraph.graph import END, START, StateGraph
from app.nodes import load_patient_node, analyse_patient_node, generate_report_node
from app.schemas import AgentState

builder = StateGraph(AgentState)

builder.add_node("load_patient",load_patient_node )
builder.add_node("analyse_patient", analyse_patient_node)
builder.add_node("report_generation", generate_report_node)

builder.add_edge(START, "load_patient")
builder.add_edge("load_patient","analyse_patient")
builder.add_edge("analyse_patient", "report_generation")
builder.add_edge("report_generation", END)

graph = builder.compile()
