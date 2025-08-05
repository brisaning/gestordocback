from abc import ABC, abstractmethod
from typing import List
from .models import Serie, Subserie, TipoDocumental

class TrdRepository(ABC):

    @abstractmethod
    def get_series(self) -> List[Serie]:
        pass

    @abstractmethod
    def get_subseries_by_serie(self, serie_id: int) -> List[Subserie]:
        pass

    @abstractmethod
    def get_tipos_documentales_by_subserie(self, subserie_id: int) -> List[TipoDocumental]:
        pass
