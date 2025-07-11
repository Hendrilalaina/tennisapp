from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.models.tournament import Tournament
from app.schemas.tournament import TournamentSchema

class TournamentRepository:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Tournament] :
        return db.query(Tournament).offset(offset).limit(limit).all()
    
    def get(self, db: Session, id: int) -> Optional[Tournament]:
        return db.query(Tournament).filter(Tournament.id == id).first()
    
    def create(self, db: Session, tournament_schema: TournamentSchema) -> Tournament :
        tournament = Tournament(name=tournament_schema.name)
        
        db.add(tournament)
        db.commit()
        db.refresh(tournament)
        return tournament
    
    def update(self, db: Session, id: int, tournament_schema: TournamentSchema) -> Optional[Tournament] :
        tournament = self.get(db, id)
        if tournament is None:
            return None
        
        tournament.name = tournament_schema.name
        db.add(tournament)
        db.commit()
        db.refresh(tournament)

        return tournament
    
    def delete(self, db: Session, id: int) -> str :
        tournament = self.get(db, id)
        if tournament is None:
            return f"Tournament with id {id} is not found"
        
        db.delete(tournament)
        db.commit()

        return f"Tournament with id {id} is deleted"
        
tournament_repository = TournamentRepository()