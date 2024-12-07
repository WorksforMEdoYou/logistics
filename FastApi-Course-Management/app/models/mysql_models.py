from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from ..database.mysql import Base

class Subscriber(Base):
    __tablename__ = "subscribers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    subscription_date = Column(DateTime)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    duration = Column(String)
    counselor_id = Column(Integer, ForeignKey("subscribers.id")) # Subscriber -> subscribers(tablename).id(tablename.id)

    counselor = relationship("Subscriber") #getting the ClassName