from app.config import settings
from app.repository import RepositoryLoader
from app.llm import llm_client

def main():
    print("=" * 60)
    print("CONFIG")
    print("=" * 60)

    print(settings.model_name)
    print(settings.temperature)
    print()

    print("=" * 60)
    print("LOADER")
    print("=" * 60)
    
    loader = RepositoryLoader()
    patient = loader.get_patient("P0009")
    print(patient)

    print()

    print("=" * 60)
    print("LLM")
    print("=" * 60)
    print(llm_client.llm.model_name)

    print()

    print("Foundation Layer Working Successfully")


if __name__ == "__main__":
    main()