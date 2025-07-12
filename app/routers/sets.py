from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.crud.set import set_repository

router = APIRouter(
    prefix='/sets',
    tags=['Sets'])

@router.get('/')
async def list_sets(db: Session = Depends(get_db)):
    return set_repository.get_all()