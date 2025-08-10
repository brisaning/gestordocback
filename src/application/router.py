from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.domain.repositories import TrdRepository
from src.infrastructure.database.connection import SessionLocal
from src.infrastructure.repositories.trd_repository import TrdRepositoryImpl
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_trd_repository(db: Session = Depends(get_db)) -> TrdRepository:
    return TrdRepositoryImpl(db)

