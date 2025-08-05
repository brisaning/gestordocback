from typing import List
from sqlalchemy.orm import Session
from src.domain.models import Serie, Subserie, TipoDocumental
from src.domain.repositories import TrdRepository
from src.infrastructure.database.models import Serie as SerieModel, Subserie as SubserieModel, TipoDocumental as TipoDocumentalModel

class TrdRepositoryImpl(TrdRepository):

    def __init__(self, db: Session):
        self.db = db

    def get_series(self) -> List[Serie]:
        return self.db.query(SerieModel).all()

    def get_subseries_by_serie(self, serie_id: int) -> List[Subserie]:
        return self.db.query(SubserieModel).filter(SubserieModel.serie_id == serie_id).all()

    def get_tipos_documentales_by_subserie(self, subserie_id: int) -> List[TipoDocumental]:
        return self.db.query(TipoDocumentalModel).filter(TipoDocumentalModel.subserie_id == subserie_id).all()
