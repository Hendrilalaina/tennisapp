from typing import List, Optional
from sqlalchemy import case, func
from sqlalchemy.orm import Session

from app.db.models.match import Match
from app.db.models.set import Set
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

    def get_sets(self, db: Session, id: int):
        return db.query(Set).filter(Set.match_id == id).all()
    
    def get_set_wins(self, db: Session, id: int):
        set_wins = db.query(
            func.sum(case((Set.player1_games > Set.player2_games, 1), else_=0)).label('player1_wins'),
            func.sum(case((Set.player2_games > Set.player1_games, 1), else_=0)).label('player2_wins')
        ).filter(Set.match_id == id).one()

        return {
            "player1_wins": set_wins.player1_wins,
            "player2_wins": set_wins.player2_wins
        }


match_repository = MatchRepository()