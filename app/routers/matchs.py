from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.match import match_repository

router = APIRouter(
    prefix='/match',
    tags=['Matches'])

@router.get('/')
async def list_matches(db: Session = Depends(get_db)):
    return match_repository.get_all(db)
