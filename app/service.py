"""User service layer for business logic operations."""
from sqlalchemy.orm import Session
from . import user, schemas
from .user import User


def create_user(db: Session, user_dto: schemas.UserCreate):
    """Create a new user in the database.

     Args:
         db: Database session
         user_data: User creation data

     Returns:
         Created user instance
         :param db:
         :param user_dto:
     """

    db_user = User(name=user_dto.name, email=user_dto.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    """Get all users from the database.

   Args:
       db: Database session

   Returns:
       List of all users
   """
    return db.query(user.User).all()
