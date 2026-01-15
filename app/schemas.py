"""
Pydantic schemas for data validation and serialization.

This module contains Pydantic models used for request/response validation
and data serialization in the FastAPI application.
"""
from pydantic import BaseModel


class UserCreate(BaseModel):  # pylint: disable=too-few-public-methods
    """
    Schema for user creation requests.
    
    Used to validate incoming data when creating a new user.
    Contains all the required fields for user registration.
    """
    name: str
    email: str
    description: str


class User(UserCreate):  # pylint: disable=too-few-public-methods
    """
    Schema for user responses.
    
    Extends UserCreate with additional fields that are present
    in the database model but not required for creation.
    Used for API responses containing user data.
    """
    id: int

    class Config:  # pylint: disable=too-few-public-methods
        """
        Pydantic configuration class.
        
        Configures the model to work with SQLAlchemy ORM objects
        by enabling from_attributes mode (formerly orm_mode).
        """
        from_attributes = True
