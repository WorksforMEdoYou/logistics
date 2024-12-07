from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from ..database.mongo import db
from ..models.mongo_models import Appointment
from ..schemas.appointment import AppointmentCreate, Appointment
from ..auth.oauth2 import oauth2_scheme

# MONGODB

router = APIRouter()

@router.post("/appointments/", response_model=Appointment)
def create_appointment(appointment: AppointmentCreate):
    appointment_dict = appointment.dict()
    appointment_id = db.appointments.insert_one(appointment_dict).inserted_id
    return {**appointment_dict, "id": str(appointment_id)}

@router.get("/appointments/{appointment_id}", response_model=Appointment)
def read_appointment(appointment_id: str):
    appointment = db.appointments.find_one({"_id": ObjectId(appointment_id)})
    if appointment is None:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {**appointment, "id": str(appointment["_id"])}