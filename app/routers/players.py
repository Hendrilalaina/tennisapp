from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.crud.player import player_repository
from app.schemas.player import PlayerCreate, PlayerUpdate
from app.db.session import get_db

router = APIRouter(
    prefix='/players',
    tags=['Players'])

@router.get('/')
async def list_players(db: Session = Depends(get_db)):
    return player_repository.get_all(db)

@router.get('/{id}')
async def get_player(id: int, db: Session = Depends(get_db)):
    return player_repository.get(db, id)

@router.post('/')
async def create_player(player: PlayerCreate, db: Session = Depends(get_db)):
    return player_repository.create(db, player)

@router.put('/{id}')
async def update_player(id: int, player: PlayerUpdate, db: Session = Depends(get_db)):
    return player_repository.update(db, id, player)

@router.delete('/{id}')
async def delete_player(id: int, db: Session = Depends(get_db)):
    return player_repository.delete(db, id)