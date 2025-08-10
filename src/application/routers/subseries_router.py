from fastapi import APIRouter, Depends
from typing import List
from src.domain.model import Subserie
from src.domain.repositories import TrdRepository
from src.infrastructure.database.session_db import get_trd_repository
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter()

@router.get("/subseries/{serie_id}", response_model=List[Subserie])
def get_subseries_by_serie(serie_id: int, repo: TrdRepository = Depends(get_trd_repository), current_user: User = Depends(get_current_user)):
    return repo.get_subseries_by_serie(serie_id)