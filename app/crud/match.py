from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.models.match import Match
from app.schemas.match import MatchCreate
from app.crud.player import player_repository

class MatchRepository:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Match] :
        return db.query(Match).offset(offset).limit(limit).all()
    
    def get(self, db: Session, id: int) -> Optional[Match] :
        return db.query(Match).filter(Match.id == id).first()

    def create(self, db: Session, match_create: MatchCreate) -> Match :
        match = Match(
            player_1 = match_create.player_1,
            player_2 = match_create.player_2,
            tournament_id = match_create.tournament,
            year = match_create.year)
        
        db.add(match)
        db.commit()
        db.refresh(match)
        return match


match_repository = MatchRepository()