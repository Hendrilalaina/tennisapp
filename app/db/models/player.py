from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.db.session import Base

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100))
    sexe = Column(Enum('M', 'F'), nullable=False)

    player_1 = relationship('Match', foreign_keys='Match.player_1', back_populates='p_1')
    player_2 = relationship('Match', foreign_keys='Match.player_2', back_populates='p_2')
