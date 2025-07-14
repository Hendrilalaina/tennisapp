from pydantic import Field, BaseModel
from typing import Optional

from app.schemas.player import PlayerResponse
from app.schemas.tournament import TournamentResponse

class MatchCreate(BaseModel):
    player_1: int = Field()
    player_2: int = Field()
    tournament: Optional[int] = Field(None)
    year: Optional[int] = Field(None)

class MatchResponse(BaseModel):
    p_1: PlayerResponse
    p_2: PlayerResponse
    tournament: Optional[TournamentResponse]
    year: Optional[int]

    class Config:
        orm_mode = True