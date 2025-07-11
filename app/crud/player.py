from typing import List, Optional
from sqlalchemy.orm import Session

from app.db.models.player import Player
from app.schemas.player import PlayerCreate, PlayerUpdate

class PlayerRepository:
    def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> List[Player]:
        return db.query(Player).offset(skip).limit(limit).all()

    def get(self, db: Session, id: int) -> Optional[Player]:
        return db.query(Player).filter(Player.id == id).first()
    
    def create(self, db: Session, player_create: PlayerCreate) -> Player :
        player = Player(
            last_name=player_create.last_name,
            first_name=player_create.first_name,
            sexe=player_create.sexe.value)
        
        db.add(player)
        db.commit()
        db.refresh(player)
        return player
    
    def update(self, db: Session, id: int, player_update: PlayerUpdate) -> Optional[Player] :
        player = self.get(db, id)
        if not player:
            return None
        
        if player_update.first_name is not None:
            player.first_name = player_update.first_name
        if player_update.last_name is not None:
            player.last_name = player_update.last_name
        if player_update.sexe is not None:
            player_update.sexe = player_update.sexe

        db.add(player)
        db.commit()
        db.refresh(player)
        return player
    
    def delete(self, db: Session, id: int) -> str:
        player = self.get(db, id)
        if not player:
            return f"Cannot find player with id {id}"
        db.delete(player)
        db.commit()
        return f"Player with id {id} is deleted"

player_repository = PlayerRepository()