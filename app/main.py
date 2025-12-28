"""
Main FastAPI application module.

This module contains the FastAPI application instance and all API endpoints
for the user management system. It handles HTTP requests and responses,
integrating with the service layer for business logic.
"""
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from .database import SESSION_LOCAL, engine, Base
from . import service, schemas

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    """
    Returns a database session.

    This function is a dependency injection (DI) mechanism for FastAPI,
    ensuring that a database session is injected into each API endpoint.
    """
    db = SESSION_LOCAL()
    try:
        yield db
    finally:
        db.close()

@app.post("/users", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user.

    Creates a new user in the database with the provided information.

    Args:
        user_data: User creation data containing name and email
        db: Database session dependency

    Returns:
        schemas.User: The created user with generated ID

    Raises:
        HTTPException: If user creation fails or email already exists
    """
    return service.create_user(db, user)

@app.get("/users", response_model=list[schemas.User])
def read_users(db: Session = Depends(get_db)):
    """
   Retrieve all users.

   Fetches and returns a list of all users from the database.

   Args:
       db: Database session dependency

   Returns:
       list[schemas.User]: List of all users in the database
   """
    return service.get_users(db)

@app.get("/health")
def health():
    """
   Health check endpoint.

   Returns the current status of the application to verify
   that the service is running and responsive.

   Returns:
       dict: A dictionary containing the application status
   """
    return {"status": "ok"}
