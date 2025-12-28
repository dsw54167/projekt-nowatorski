"""
Pydantic schemas for data validation and serialization.

This module contains Pydantic models used for request/response validation
and data serialization in the FastAPI application.
"""
from pydantic import BaseModel

class UserCreate(BaseModel):
    """
    Schema for user creation requests.

    Used to validate incoming data when creating a new user.
    Contains all the required fields for user registration.
    """
    name: str
    email: str

class User(UserCreate):
    """
   Schema for user responses.

   Extends UserCreate with additional fields that are present
   in the database model but not required for creation.
   Used for API responses containing user data.
   """
    id: int

    class Config:
        """
       Pydantic configuration class.

       Configures the model to work with SQLAlchemy ORM objects
       by enabling from_attributes mode (formerly orm_mode).
       """
        orm_mode = True
