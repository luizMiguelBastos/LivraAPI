from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict



class AutoresCreate(BaseModel):
    nome: str = Field(max_length=150)
    nacionalidade: Optional[str] = Field(default=None, max_length=150)

class AutoresUpdate(BaseModel):
    nome: Optional[str] = Field(default=None, max_length=150)
    nacionalidade: Optional[str] = Field(default=None, max_length=150)

class AutoresResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    nome: str = Field( max_length=150)
    nacionalidade: Optional[str] = Field(default=None, max_length=150)
    id: int
    criado_em: datetime