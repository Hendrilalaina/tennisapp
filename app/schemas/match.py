from pydantic import Field, BaseModel
from typing import Optional

class MatchCreate(BaseModel):
    player_1: int = Field()
    player_2: int = Field()
    tournament: Optional[int] = Field(None)
    year: Optional[int] = Field(None)
