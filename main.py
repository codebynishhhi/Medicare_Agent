from app.graph import graph
from app.schemas import AgentState

def main():
    state = AgentState(
        patient_id="P0004"
    )
    result = graph.invoke(state)
    print(result["report"])


if __name__ == "__main__":
    main()