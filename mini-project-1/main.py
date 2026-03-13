from fastapi import FastAPI, HTTPException
from models import Patient, Appointment
import asyncio
from typing import List

app = FastAPI()

patients: List[Patient] = []

@app.get("/patients/", response_model=List[Patient])
async def read_patient_information():
    await asyncio.sleep(1)
    return patients

@app.get("/patients/{patient_id}", response_model=Patient)
async def read_patient_information_by_id(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code = 404, detail = "Patient not found")



