from abc import ABC, abstractmethod
from typing import List
from src.domain.models.series_model import SerieModel


class SeriesRepository(ABC):

    @abstractmethod
    def get_series(self) -> List[SerieModel]:
        pass

    @abstractmethod
    def get_serie_by_id(self, id: int) -> SerieModel:
        pass

    @abstractmethod
    def get_serie_by_serie(self, serie_id: int) -> List[SerieModel]:
        pass

    @abstractmethod
    def set_serie(self, serie: SerieModel) -> SerieModel:
        pass

    @abstractmethod
    def update_serie(self, seri_id: int, serie: SerieModel) -> SerieModel:
        pass

    @abstractmethod
    def remove_serie(self, id: int) -> bool:
        pass