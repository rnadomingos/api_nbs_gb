from sqlalchemy.exc import ArgumentError
from sqlalchemy.orm import Session

from src.data import models, schemas
from src.infra.security import get_password_hash, verify_password

def get_user(db: Session, username: str):
    
    if not username:
        raise ArgumentError("Must provide user_id or email")
    
    query = db.query(models.User).filter(models.User.username == username)
    
    return query.first()

def get_users(
        db: Session, 
        skip: int = 0, 
        limit: int = 100
        ):
    users = db.query(models.User).offset(skip).limit(limit).all()
    print("get_users result:", users)
    return users

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username = user.username,
        role = user.role,
        password = get_password_hash(user.password),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def authenticate(db: Session, username: str, password: str):
    db_user = get_user(db=db, username=username)
    if not db_user or not verify_password(password, db_user.password):
        return None
    return db_user