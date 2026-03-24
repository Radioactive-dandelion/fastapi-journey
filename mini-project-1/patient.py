from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import Patient
import asyncio
from typing import List
from database import managed_db

patient_router = APIRouter()

templates = Jinja2Templates(directory="mini-project-1/templates") #There is a problem with the directory, it needs to be replaced with templates = Jinja2Templates(directory="templates") and use cd mini-project-1, uvicorn main:app --reload


@patient_router.get("/patients/", response_model=List[Patient])
async def read_patient_information():
    await asyncio.sleep(1)
    with managed_db() as db:
        return db.get_all()


@patient_router.get("/patients/{patient_id}", response_model=Patient)
async def read_patient_information_by_id(patient_id: int):
    with managed_db() as db:
        patient = db.get(patient_id)

    if not patient:
        raise HTTPException(
        status_code=404,
        detail=f"Patient with ID {patient_id} was not found"
    )
    return patient

@patient_router.post("/patients/", response_model=Patient)
async def add_patient(patient: Patient):
    with managed_db() as db:
        new_id = db.create(patient)
        created_patient = db.get(new_id)

    return created_patient

@patient_router.put("/patients/{patient_id}", response_model=Patient)
async def update_patient(patient_id: int, updated_patient: Patient):
    with managed_db() as db:
        existing = db.get(patient_id)

        if not existing:
            raise HTTPException(
                status_code=404,
                detail=f"Patient with ID {patient_id} was not found"
            )

        updated = db.update(patient_id, updated_patient)

    return updated  


@patient_router.delete("/patients/{patient_id}")
async def remove_patient(patient_id: int):
    await asyncio.sleep(3)
    with managed_db() as db:
        existing = db.get(patient_id)

        if not existing:
            raise HTTPException(
                status_code=404,
                detail=f"Patient with ID {patient_id} was not found"
            )

        db.delete(patient_id)

    return {"message": "Patient deleted"}

@patient_router.get("/home", response_class=HTMLResponse)
async def home(request: Request):
    with managed_db() as db:
        patients = db.get_all()
        
    return templates.TemplateResponse("home.html", {
        "request": request,
        "patients": patients
    })

@patient_router.get("/patient/{patient_id}", response_class=HTMLResponse)
async def get_patient_page(request: Request, patient_id: int):
    with managed_db() as db:
        patient = db.get(patient_id)

    if not patient:
        raise HTTPException(
            status_code=404,
            detail=f"Patient with ID {patient_id} was not found"
        )

    return templates.TemplateResponse("patient.html", {
        "request": request,
        "patient": patient
    })