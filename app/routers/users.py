from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models import models
from app.schemas import schemas
from typing import List

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/doctors", response_model=List[schemas.ShowUser])
def get_doctors(db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.role == "doctor").all()

@router.get("/patients", response_model=List[schemas.ShowUser])
def get_patients(db: Session = Depends(get_db)):
    return db.query(models.User).filter(models.User.role == "patient").all()
