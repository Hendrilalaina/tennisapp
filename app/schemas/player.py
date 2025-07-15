from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum

class Sexe(Enum):
    MALE = 'M'
    FEMALE = 'F'

class PlayerCreate(BaseModel):
    first_name: str = Field(min_length=3, max_length=100)
    last_name: Optional[str] = Field(min_length=3, max_length=100)
    sexe: Sexe = Field()

class PlayerUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=3, max_length=100)
    last_name: Optional[str] = Field(None, min_length=3, max_length=100)
    sexe: Optional[Sexe] = None

class PlayerResponse(BaseModel):
    first_name: str
    last_name: str
    sexe: str

    class Config:
        from_attributes = True