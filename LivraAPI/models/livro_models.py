import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from core import Base

class Livro(Base):
    __tablename__ = 'livros'

    id: Mapped[int] = mapped_column (primary_key=True)
    titulo: Mapped[str] = mapped_column (nullable=False)
    ano_publicado: Mapped[int] = mapped_column (nullable=False)
    autor_id:Mapped[int] = mapped_column (ForeignKey('autores.id'), nullable=False)
    disponivel: Mapped[bool] = mapped_column (nullable=False, default=True)
    criado_em: Mapped[datetime.datetime] = mapped_column (default=datetime.datetime.now)