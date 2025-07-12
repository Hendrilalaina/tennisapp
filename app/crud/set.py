from typing import List
from sqlalchemy.orm import Session

from app.db.models.set import Set
from app.schemas.set import SetCreate

class SetRepository:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Set] :
        return db.query(Set).offset(offset).limit(limit).all()
    
    def create(self, db: Session, set_create: SetCreate) -> Set:
        set = Set()
        set.match_id = set_create.match_id
        set.set_number = set_create.set_number
        set.player1_games = set_create.player1_games
        set.player2_games = set_create.player2_games

        db.add(set)
        db.commit()
        db.refresh(set)

        return set
set_repository = SetRepository()