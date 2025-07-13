from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.tournament import tournament_repository
from app.schemas.tournament import TournamentResponse, TournamentSchema

router = APIRouter(
    prefix='/tournaments',
    tags=['Tournaments'])

@router.get('/', response_model=List[TournamentResponse])
async def list_tournaments(db: Session = Depends(get_db)):
    return tournament_repository.get_all(db)

@router.post('/', response_model=TournamentResponse)
async def create_tournament(tournament: TournamentSchema, db: Session = Depends(get_db)):
    return tournament_repository.create(db, tournament)

@router.get('/{id}', response_model=TournamentResponse)
async def get_tournament(id: int, db: Session = Depends(get_db)):
    return tournament_repository.get(db, id)

@router.put('/{id}', response_model=Optional[TournamentResponse])
async def update_tournament(id: int, tournament: TournamentSchema, db: Session = Depends(get_db)):
    return tournament_repository.update(db, id, tournament)

@router.delete('/{id}')
async def delete_tournament(id: int, db: Session = Depends(get_db)):
    return tournament_repository.delete(db, id)