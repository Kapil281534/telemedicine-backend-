from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import models
from app.schemas import schemas
from typing import List

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=schemas.ShowAppointment)
def create_appointment(appt: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    new_appt = models.Appointment(
        patient_id=appt.patient_id,
        doctor_id=appt.doctor_id
    )
    db.add(new_appt)
    db.commit()
    db.refresh(new_appt)
    return new_appt

@router.get("/user/{user_id}", response_model=List[schemas.ShowAppointment])
def get_user_appointments(user_id: int, db: Session = Depends(get_db)):
    return db.query(models.Appointment).filter(
        (models.Appointment.patient_id == user_id) | (models.Appointment.doctor_id == user_id)
    ).all()
