from pydantic import BaseModel
from datetime import datetime

# MONGO DB
class AssessmentBase(BaseModel):
    appointment_id: str  # MongoDB ObjectId
    assessment_details: str
    due_date: datetime

class AssessmentCreate(AssessmentBase):
    pass

class Assessment(AssessmentBase):
    id: str  # MongoDB ObjectId

    class Config:
        orm_mode = True