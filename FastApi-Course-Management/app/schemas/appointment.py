from pydantic import BaseModel
from datetime import datetime

# MONGO DB
class AppointmentBase(BaseModel):
    subscriber_id: int
    course_id: int
    appointment_date: datetime
    status: str

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: str  # MongoDB ObjectId can be string

    class Config:
        orm_mode = True