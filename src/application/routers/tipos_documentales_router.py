from fastapi import APIRouter, Depends
from typing import List
from src.domain.model import TipoDocumental
from src.domain.repositories import TrdRepository
from src.infrastructure.database.session_db import get_trd_repository
from src.infrastructure.security.keycloak import get_current_user, User

router = APIRouter(
    tags=["Tipos Documentales"],
    responses={404: {"description": "Not found"}},
    dependencies=[Depends(get_current_user)],
    include_in_schema=True
)

@router.get("/tipos-documentales", response_model=List[TipoDocumental])
async def get_tipos_documentales(repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_tipos_documentales()

@router.get("/tipos-documentales/{id}", response_model=TipoDocumental)
async def get_tipo_documental(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_tipo_documental(id)

@router.get("/tipos-documentales/tipo/{tipo}", response_model=List[TipoDocumental])
async def get_tipos_documentales_by_subserie(tipo: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.get_tipos_documentales_by_subserie(tipo)

@router.post("/tipos-documentales", response_model=TipoDocumental)
async def create_tipo_documental(tipo_documental: TipoDocumental, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.create_tipo_documental(tipo_documental)

@router.put("/tipos-documentales/{id}", response_model=TipoDocumental)
async def update_tipo_documental(id: int, tipo_documental: TipoDocumental, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.update_tipo_documental(id, tipo_documental)

@router.delete("/tipos-documentales/{id}", response_model=TipoDocumental)
async def delete_tipo_documental(id: int, repo: TrdRepository = Depends(get_trd_repository)):
    return repo.delete_tipo_documental(id)