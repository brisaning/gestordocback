from fastapi import APIRouter, Depends
from typing import List
from src.domain.model import Subserie
from src.domain.repositories import TrdRepository
from src.infrastructure.database.session_db import get_trd_repository
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter(
    prefix="/api/v1",
    tags=["Subseries"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)],
    include_in_schema=True
)

@router.get("/subseries", response_model=List[Subserie])
async def get_subseries(repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_subseries()

@router.get("/subseries/id/{id}", response_model=Subserie)
async def get_subseries_by_id(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_subseries_by_id(id)

@router.get("/subseries/{serie_id}", response_model=List[Subserie])
async def get_subseries_by_serie(serie_id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_subseries_by_serie(serie_id)

@router.post("/subseries", response_model=Subserie)
async def create_subserie(subserie: Subserie, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.create_subserie(subserie)

@router.put("/subseries/{id}", response_model=Subserie)
async def update_subserie(id: int, subserie: Subserie, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.update_subserie(id, subserie)

@router.delete("/subseries/{id}", response_model=Subserie)
async def delete_subserie(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.delete_subserie(id)
