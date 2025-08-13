from pydantic import BaseModel

class TipoDocumentalModel(BaseModel):
    id: int
    nombre: str
    subserie_id: int

    class Config:
        orm_mode = True
