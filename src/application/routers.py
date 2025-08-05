from fastapi import APIRouter, Depends
from typing import List
from sqlalchemy.orm import Session
from src.domain.models import Serie, Subserie, TipoDocumental
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

@router.get("/series", response_model=List[Serie])
def get_series(repo: TrdRepository = Depends(get_trd_repository), current_user: User = Depends(get_current_user)):
    return repo.get_series()

@router.get("/subseries/{serie_id}", response_model=List[Subserie])
def get_subseries_by_serie(serie_id: int, repo: TrdRepository = Depends(get_trd_repository), current_user: User = Depends(get_current_user)):
    return repo.get_subseries_by_serie(serie_id)

@router.get("/tipos-documentales/{subserie_id}", response_model=List[TipoDocumental])
def get_tipos_documentales_by_subserie(subserie_id: int, repo: TrdRepository = Depends(get_trd_repository), current_user: User = Depends(get_current_user)):
    return repo.get_tipos_documentales_by_subserie(subserie_id)
