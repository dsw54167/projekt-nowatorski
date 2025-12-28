from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SessionLocal, engine, Base
from . import service, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return service.create_user(db, user)

@app.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    return service.get_users(db)

@app.get("/health")
def health():
    return {"status": "ok"}

