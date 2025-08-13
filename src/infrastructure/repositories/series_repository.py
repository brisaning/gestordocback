from typing import List
from sqlalchemy.orm import Session
from src.domain.models.series_model import SerieModel
from src.infrastructure.database.model.series_bd_model import SerieBdModel
from src.domain.repository.series_repository import SeriesRepository

class SeriesRepositoryImpl(SeriesRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_series(self) -> List[SerieModel]:
        return self.db.query(SerieBdModel).all()
    
    def get_serie_by_id(self, id: int) -> SerieModel:
        return self.db.query(SerieBdModel).filter(SerieBdModel.id == id).first()
    
    def get_serie_by_serie(self, serie_id: int) -> List[SerieModel]:
        return self.db.query(SerieBdModel).filter(SerieBdModel.id == serie_id).all()
    
    def set_serie(self, serie: SerieModel) -> SerieModel:
        new_serie = SerieBdModel(nombre=serie.nombre)
        self.db.add(new_serie)
        self.db.commit()
        self.db.refresh(new_serie)
        return new_serie
    
    def delete_serie(self, serie_id: int) -> None:
        serie = self.db.query(SerieBdModel).filter(SerieBdModel.id == serie_id).first()
        self.db.delete(serie)
        self.db.commit()
    
    def update_serie(self, serie_id: int, serie: SerieModel) -> SerieModel:
        serie_db = self.db.query(SerieBdModel).filter(SerieBdModel.id == serie_id).first()
        serie_db.nombre = serie.nombre
        self.db.commit()
        self.db.refresh(serie_db)
        return serie_db