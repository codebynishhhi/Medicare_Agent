from app.config import settings
from app.schemas import PatientRecord
from typing import Dict, Any
import csv

class RepositoryLoader:
    """
    Responsible only for loading patient data using an in-memory dictionary.
    """
    def __init__(self):

        # dictonary lookup to store csv data
        self._patient : PatientRecord = {}

        with open(settings.data_path, newline="", mode="r", encoding="utf-8") as csv_file:
            patient_lookup = csv.DictReader(csv_file)
            for row in patient_lookup:
                patient = PatientRecord(**row)
                self._patient[patient.patient_id] = patient

    def get_patient(self, id:int) -> PatientRecord:
        patient = self._patient.get(id) 
        if patient is None:
            raise ValueError("Patient with id : {id} not found!")
        return patient
    

repo_data = RepositoryLoader()

            

