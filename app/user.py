"""User model definition."""
from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    """User database model.

   Represents a user in the database with basic information
   like ID and email address.
   """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
