from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.set import set_repository
from app.crud.match import match_repository
from app.schemas.set import SetCreate

router = APIRouter(
    prefix='/sets',
    tags=['Sets'])

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
    
    set.validate_set()
    return set_repository.create(db, set)
