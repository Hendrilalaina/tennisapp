from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.match import match_repository
from app.crud.player import player_repository
from app.schemas.match import MatchCreate

router = APIRouter(
    prefix='/match',
    tags=['Matches'])

@router.get('/')
async def list_matches(db: Session = Depends(get_db)):
    return match_repository.get_all(db)

@router.post('/')
async def create_match(match: MatchCreate, db: Session = Depends(get_db)):
    player_1 = player_repository.get(db, id=match.player_1)
    if player_1 is None:
        raise HTTPException(
            status_code=404,
            detail="Player 1 is not found")
    
    player_2 = player_repository.get(db, id=match.player_2)
    if player_2 is None:
        raise HTTPException(
            status_code=404,
            detail="Player 2 is not found")
    
    if player_1 == player_2:
        raise HTTPException(
            status_code=403,
            detail="Two players can not be same")
    
    return match_repository.create(db, match)