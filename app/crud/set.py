from typing import List
from sqlalchemy.orm import Session

from app.db.models.set import Set

class SetRepository:
    def get_all(self, db: Session, offset: int = 0, limit: int = 100) -> List[Set] :
        return db.query(Set).offset(offset).limit(limit).all()
    
set_repository = SetRepository()