from pydantic import BaseModel

class SubserieModel(BaseModel):
    id: int
    nombre: str
    serie_id: int

    class Config:
        orm_mode = True