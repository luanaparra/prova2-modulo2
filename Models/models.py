from sqlalchemy import Table, Column, Integer, String, List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import mapper

class Base(DeclarativeBase):
    pass

class Game(Base):
    __tablename__ = "eletronic_games"
    id = Column(Integer, primary_key=True)
    nome = Column(String, unique=True)
    plataforma = Column(String, unique=True)
    preco = Column(String, unique=True)
    quantidade = Column(String, unique=True)

    def __init__(self, nome=None, plataforma=None, preco=None, quantidade=None):
        self.id = id
        self.nome = nome
        self.plataforma = plataforma
        self.preco = preco
        self.quantidade = quantidade

    def __repr__(self):
        return f'<Game {self.nome!r}>'


