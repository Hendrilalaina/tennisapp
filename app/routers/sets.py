from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.set import set_repository
from app.crud.match import match_repository
from app.schemas.set import SetCreate

router = APIRouter(
    prefix='/sets',
    tags=['Sets'])

def validate_set(set: SetCreate):

    if set.player1_games < 6 and set.player2_games < 6:
        raise HTTPException(
            status_code=400,
            detail="Invalid games")

    if set.player1_games == 5 and set.player2_games == 6:
        raise HTTPException(
            status_code=400,
            detail="Invalid games")
    
    if set.player1_games == 6 and set.player2_games == 5:
        raise HTTPException(
            status_code=400,
            detail="Invalid games")

    if set.player1_games == 7:
        if set.player2_games < 5 or set.player2_games > 6:
            raise HTTPException(
                status_code=400,
                detail="Invalid games")
        
    if set.player2_games == 7:
        if set.player1_games < 5 or set.player1_games > 6:
            raise HTTPException(
                status_code=400,
                detail="Invalid games")

@router.get('/')
async def list_sets(db: Session = Depends(get_db)):
    return set_repository.get_all(db)

@router.post('/')
async def create_set(set: SetCreate, db: Session = Depends(get_db)):
    match = match_repository.get(db, set.match_id)
    if match is None:
        raise HTTPException(
            status_code=404,
            detail="Match is not found")
    
    validate_set(set)
    return set_repository.create(db, set)
