from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from ..database.mysql import SessionLocal
from ..models.mysql_models import Subscriber
from ..schemas.subscriber import SubscriberCreate, Subscriber
from ..auth.jwt import create_access_token, verify_password
from ..auth.oauth2 import oauth2_scheme

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/subscribers/", response_model=Subscriber)
def create_subscriber(subscriber: SubscriberCreate, db: Session = Depends(get_db)):
    db_subscriber = Subscriber(**subscriber.dict())
    db.add(db_subscriber)
    db.commit()
    db.refresh(db_subscriber)
    return db_subscriber

@router.get("/subscribers/{subscriber_id}", response_model=Subscriber)
def read_subscriber(subscriber_id: int, db: Session = Depends(get_db)):
    subscriber = db.query(Subscriber).filter(Subscriber.id == subscriber_id).first()
    if subscriber is None:
        raise HTTPException(status_code=404, detail="Subscriber not found")
    return subscriber

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(Subscriber).filter(Subscriber.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.email })
    return {"access_token": access_token, "token_type": "bearer"}