from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Patient
import asyncio
from typing import List

patient_router = APIRouter()

templates = Jinja2Templates(directory="mini-project-1/templates") #There is a problem with the directory, it needs to be replaced with templates = Jinja2Templates(directory="templates") and use cd mini-project-1, uvicorn main:app --reload

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
    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} was not found"
    )

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
    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} was not found"
    )
        


@patient_router.delete("/patients/{patient_id}")
async def remove_patient(patient_id: int):
    await asyncio.sleep(3)
    for idx, patient in enumerate(patients):
        if patient.id == patient_id:
            patients.pop(idx)
            return {"message": "Patient deleted"}
    raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} was not found"
    )

@patient_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("home.html", {
        "request": request,
        "patients": patients
    })

@patient_router.get("/patient/{patient_id}", response_class=HTMLResponse)
async def get_patient_page(request: Request, patient_id: int):
    for patient in patients:
        if patient.id == patient_id:
            return templates.TemplateResponse("patient.html", {
                "request": request,
                "patient": patient
            })
    raise HTTPException(
    status_code=404,
    detail=f"Patient with ID {patient_id} was not found"
)