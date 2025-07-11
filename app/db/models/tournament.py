from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Tournament(Base):
    __tablename__ = 'tournaments'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)