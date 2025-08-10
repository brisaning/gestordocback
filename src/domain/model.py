from pydantic import BaseModel

class Serie(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True

class Subserie(BaseModel):
    id: int
    nombre: str
    serie_id: int

    class Config:
        orm_mode = True

class TipoDocumental(BaseModel):
    id: int
    nombre: str
    subserie_id: int

    class Config:
        orm_mode = True
