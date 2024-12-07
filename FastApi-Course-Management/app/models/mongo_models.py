from pydantic import BaseModel
from bson import ObjectId
from datetime import datetime

class Appointment(BaseModel):
    subscriber_id: int
    course_id: int
    appointment_date: datetime
    status: str

class EvaluationReport(BaseModel):
    appointment_id: ObjectId
    report_details: str
    date_created: datetime

class Assessment(BaseModel):
    appointment_id: ObjectId
    assessment_details: str
    due_date: datetime