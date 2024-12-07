from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from ..database.mongo import db
from ..models.mongo_models import EvaluationReport
from ..schemas.evaluation_report import EvaluationReportCreate, EvaluationReport
from ..auth.oauth2 import oauth2_scheme

router = APIRouter()

@router.post("/evaluation_reports/", response_model=EvaluationReport)
def create_evaluation_report(report: EvaluationReportCreate):
    report_dict = report.dict()
    report_id = db.evaluation_reports.insert_one(report_dict).inserted_id
    return {**report_dict, "id": str(report_id)}

@router.get("/evaluation_reports/{report_id}", response_model=EvaluationReport)
def read_evaluation_report(report_id: str):
    report = db.evaluation_reports.find_one({"_id": ObjectId(report_id)})
    if report is None:
        raise HTTPException(status_code=404, detail="Evaluation report not found")
    return {**report, "id": str(report["_id"])}