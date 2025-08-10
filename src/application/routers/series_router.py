from fastapi import APIRouter, Depends
from typing import List
from src.domain.models.series_model import SerieModel
from src.domain.repositories import TrdRepository
from src.infrastructure.database.session_db import get_trd_repository
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter(
    prefix="/api/v1",
    tags=["Series"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)],
    include_in_schema=True
)

@router.get("/series", response_model=List[SerieModel])
async def get_series(repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_series()

@router.get("/series/{id}", response_model=SerieModel)
async def get_series_by_id(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_series_by_id(id)

@router.get("/series/code/{code}", response_model=SerieModel)
async def get_series_by_code(code: str, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_series_by_code(code)

@router.post("/series", response_model=SerieModel)
async def create_serie(serie: SerieModel, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.create_serie(serie)

@router.put("/series/{id}", response_model=SerieModel)
async def update_serie(id: int, serie: SerieModel, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.update_serie(id, serie)

@router.delete("/series/{id}")
async def delete_serie(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.delete_serie(id)