from fastapi import APIRouter, Depends
from typing import List
from src.domain.models.series_model import SerieModel
from src.domain.repositories import TrdRepository
from src.infrastructure.database.session_db import get_trd_repository
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter()

@router.get("/series", response_model=List[SerieModel])
async def get_series(repo: TrdRepository = Depends(get_trd_repository), current_user: User = Depends(get_current_user)):
    return repo.get_series()