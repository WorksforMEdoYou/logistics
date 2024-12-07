from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database.mysql import SessionLocal
from ..models.mysql_models import Course
from ..schemas.course import CourseCreate, Course
from ..auth.oauth2 import oauth2_scheme

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/courses/", response_model=Course)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course is None:
        raise HTTPException(status_code=404 , detail="Course not found")
    return course