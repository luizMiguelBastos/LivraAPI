import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core import Base

class Autores(Base):
    __tablename__ = 'autores'

    id: Mapped[int] = mapped_column (primary_key=True)
    nome: Mapped[str] = mapped_column (nullable=False)
    nacionalidade: Mapped[int] = mapped_column (nullable=False)
    criado_em: Mapped[datetime.datetime] = mapped_column (default=datetime.datetime.now)