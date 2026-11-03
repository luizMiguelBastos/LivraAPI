from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, field_validator, ConfigDict


class LivrosCreate(BaseModel):
    titulo: str = Field(max_length=150)
    ano_publicado: int = Field()
    autor_id: int = Field()

    @field_validator('ano_publicado')
    @classmethod
    def ano_publicado(cls, ano: int) -> int:
        ano_atual = datetime.now().year
        if ano > ano_atual:
            raise ValueError("O ano de publicação não pode ser maior que o ano atual")
        return ano

class LivrosUpdate(BaseModel):
    titulo: Optional[str] = Field(default=None, max_length=150)
    ano_publicado: Optional[int] = Field(default=None)
    autor_id: Optional[int] = Field(default=None)

    @field_validator('titulo', 'ano_publicado', 'autor_id')
    @classmethod
    def validar_nao_nulo(cls, valor):
        if valor is None:
            raise ValueError("O campo não pode ser nulo")
        return valor

    @field_validator('ano_publicado')
    @classmethod
    def validar_ano(cls, ano: int) -> int:
        if ano > datetime.now().year:
            raise ValueError("O ano de publicação não pode ser maior que o ano atual")
        return ano

class LivrosResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    titulo: str
    ano_publicado: int
    autor_id: int
    id: int
    disponivel: bool
    criado_em: datetime


