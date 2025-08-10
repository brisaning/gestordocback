from pydantic import BaseModel

class SerieModel(BaseModel):
    id: int
    nombre: str

    class Config:
        orm_mode = True