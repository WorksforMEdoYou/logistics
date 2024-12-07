from fastapi import FastAPI
from .database.mysql import engine, Base
from .routers import subscriber, course, appointment, evaluation_report, assessment

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(subscriber.router)
app.include_router(course.router)
app.include_router(appointment.router)
app.include_router(evaluation_report.router)
app.include_router(assessment.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Course Management System API"}