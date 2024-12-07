from pydantic import BaseModel
from datetime import datetime

# MONGO DB
class EvaluationReportBase(BaseModel):
    appointment_id: str  # MongoDB ObjectId
    report_details: str

class EvaluationReportCreate(EvaluationReportBase):
    pass

class EvaluationReport(EvaluationReportBase):
    id: str  # MongoDB ObjectId
    date_created: datetime

    class Config:
        orm_mode = True