from pydantic import Field, BaseModel

class SetCreate(BaseModel):
    match_id: int = Field()
    set_number: int = Field(ge=1, le=5)
    player1_games: int = Field(ge=0, le=7)
    player2_games: int = Field(ge=0, le=7)
