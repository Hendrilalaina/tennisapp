from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.db.session import Base

class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, index=True)
    player_1 = Column(Integer, ForeignKey('players.id'))
    player_2 = Column(Integer, ForeignKey('players.id'))
    player_winner = Column(Integer, ForeignKey('players.id'),nullable=True)
    tournament_id = Column(Integer, ForeignKey('tournaments.id'), nullable=True)
    year = Column(Integer, nullable=True)

    p_1 = relationship('Player', foreign_keys=[player_1], back_populates='player_1')
    p_2 = relationship('Player', foreign_keys=[player_2], back_populates='player_2')
    p_winner = relationship('Player', foreign_keys=[player_winner], back_populates='player_winner')
    tournament = relationship('Tournament', back_populates='match')
    sets = relationship('Set', back_populates='match')
