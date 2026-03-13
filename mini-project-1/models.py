from pydantic import BaseModel, validator, Field
from typing import List, Optional
from enum import Enum
from datetime import date, time

class Appointment_Status(str, Enum):
    scheduled = "scheduled"
    completed = "completed"
    cancelled = "cancelled"

class Appointment(BaseModel):
    id: int
    date: date
    time: time
    doctor_name: str = Field(..., min_length = 2, max_length = 50)
    status: Appointment_Status
    diagnosis: Optional[str] = None

    @validator("date")
    def check_date(cls, v):
        from datetime import date as dt_date
        if v < dt_date.today():
            raise ValueError("Appoinment date cannot be in the past")
        return v

class Patient(BaseModel):
    id: int
    name: str = Field(..., min_length = 2, max_length = 50)
    age: int = Field(..., ge = 0, le = 120)
    appointments: List[Appointment] = Field(default_factory=list)



