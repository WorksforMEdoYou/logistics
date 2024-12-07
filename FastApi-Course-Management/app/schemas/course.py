from pydantic import BaseModel

# MYSQL
class CourseBase(BaseModel):
    title: str
    description: str
    duration: str
    counselor_id: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True