from sqlalchemy import Column, Integer, String, Enum
from app.db.session import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    sexe = Column(Enum('M', 'F'), nullable=False)
