from typing import List
from sqlalchemy.orm import Session

from app.db.models.match import Match

class MatchRepository:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Match] :
        return db.query(Match).offset(offset).limit(limit).all()
    
match_repository = MatchRepository()