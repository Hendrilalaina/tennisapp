from pydantic import BaseModel, Field

class TournamentSchema(BaseModel):
    name: str = Field(min_length=3, max_length=100)

class TournamentResponse(BaseModel):
    name: str

    class Config:
        from_attributes = True