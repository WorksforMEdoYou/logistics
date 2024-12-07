from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from ..database.mongo import db
from ..models.mongo_models import Assessment
from ..schemas.assessment import AssessmentCreate, Assessment
from ..auth.oauth2 import oauth2_scheme

router = APIRouter()

@router.post("/assessments/", response_model=Assessment)
def create_assessment(assessment: AssessmentCreate):
    assessment_dict = assessment.dict()
    assessment_id = db.assessments.insert_one(assessment_dict).inserted_id
    return {**assessment_dict, "id": str(assessment_id)}

@router.get("/assessments/{assessment_id}", response_model=Assessment)
def read_assessment(assessment_id: str):
    assessment = db.assessments.find_one({"_id": ObjectId(assessment_id)})
    if assessment is None:
        raise HTTPException(status_code=404, detail="Assessment not found")
    return {**assessment, "id": str(assessment["_id"])}