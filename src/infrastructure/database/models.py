from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .connection import Base

class Serie(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)

    subseries = relationship("Subserie", back_populates="serie")

class Subserie(Base):
    __tablename__ = "subseries"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    serie_id = Column(Integer, ForeignKey("series.id"))

    serie = relationship("Serie", back_populates="subseries")
    tipos_documentales = relationship("TipoDocumental", back_populates="subserie")

class TipoDocumental(Base):
    __tablename__ = "tipos_documentales"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    subserie_id = Column(Integer, ForeignKey("subseries.id"))

    subserie = relationship("Subserie", back_populates="tipos_documentales")
