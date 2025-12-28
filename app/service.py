from sqlalchemy.orm import Session
from . import user, schemas
from .user import User


def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(user.User).all()
