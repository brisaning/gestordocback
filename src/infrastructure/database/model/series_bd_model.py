from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.infrastructure.database.connection import Base


class SerieBdModel(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    subseries = relationship("Subserie", back_populates="serie")