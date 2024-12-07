from pydantic import BaseModel
from datetime import datetime

# MYSQL 
class SubscriberBase(BaseModel):
    name: str
    email: str
    phone: str

class SubscriberCreate(SubscriberBase): #not adding the extra parameters just inheriting the SubscriberBase
    pass

class Subscriber(SubscriberBase):
    id: int
    subscription_date: datetime

    class Config:
        orm_mode = True