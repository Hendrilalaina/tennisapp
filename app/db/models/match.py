from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, index=True)
    player_1 = Column(Integer, ForeignKey('players.id'), primary_key=True)
    player_2 = Column(Integer, ForeignKey('players.id'), primary_key=True)
    player_winner = Column(Integer, nullable=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'))
    year = Column(Integer, unique=True)

    p_1 = relationship('Player', foreign_keys=[player_1], back_populates='player_1')
    p_2 = relationship('Player', foreign_keys=[player_2], back_populates='player_2')
    tournament = relationship('Tournament', back_populates='match')
    
