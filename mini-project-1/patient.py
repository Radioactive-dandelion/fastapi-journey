from fastapi import APIRouter, HTTPException
from models import Patient
import asyncio
from typing import List

patient_router = APIRouter()

patients: List[Patient] = []

@patient_router.get("/patients/", response_model=List[Patient])
async def read_patient_information():
    await asyncio.sleep(1)
    return patients

@patient_router.get("/patients/{patient_id}", response_model=Patient)
async def read_patient_information_by_id(patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code = 404, detail = "Patient not found")

@patient_router.post("/patients/", response_model=Patient)
async def add_patient(patient: Patient):
    patients.append(patient)
    return patient 

@patient_router.put("/patients/{patient_id}", response_model=Patient)
async def update_patient(patient_id: int, updated_patient: Patient):
    for idx, patient in enumerate(patients):
        if patient.id == patient_id:
            patients[idx] = updated_patient
            return updated_patient
    raise HTTPException(status_code = 404, detail = "Patient not found")
        


@patient_router.delete("/patients/{patient_id}")
async def remove_patient(patient_id: int):
    await asyncio.sleep(3)
    for idx, patient in enumerate(patients):
        if patient.id == patient_id:
            patients.pop(idx)
            return {"message": "Patient deleted"}
    raise HTTPException(status_code = 404, detail = "Patient not found")