import datetime
from typing import Optional
from sqlalchemy.orm import Mapped, mapped_column
from core import Base

class Autores(Base):
    __tablename__ = 'autores'

    id: Mapped[int] = mapped_column (primary_key=True)
    nome: Mapped[str] = mapped_column (nullable=False)
    nacionalidade: Mapped[Optional[str]] = mapped_column ()
    criado_em: Mapped[datetime.datetime] = mapped_column (default=datetime.datetime.now)