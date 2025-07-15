from fastapi import HTTPException
from pydantic import Field, BaseModel

class SetCreate(BaseModel):
    match_id: int = Field()
    set_number: int = Field(ge=1, le=5)
    player1_games: int = Field(ge=0, le=7)
    player2_games: int = Field(ge=0, le=7)

    def validate_set(self):

        if self.player1_games < 6 and self.player2_games < 6:
            raise HTTPException(
                status_code=400,
                detail="Invalid games")

        if self.player1_games == 5 and self.player2_games == 6:
            raise HTTPException(
                status_code=400,
                detail="Invalid games")
        
        if self.player1_games == 6 and self.player2_games == 5:
            raise HTTPException(
                status_code=400,
                detail="Invalid games")

        if self.player1_games == 7:
            if self.player2_games < 5 or self.player2_games > 6:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid games")
            
        if self.player2_games == 7:
            if self.player1_games < 5 or self.player1_games > 6:
                raise HTTPException(
                    status_code=400,
                    detail="Invalid games")

