from sqlalchemy import Column, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import relationship

from app.db.session import Base

class Set(Base):
    __tablename__ = 'sets'

    id = Column(Integer, primary_key=True, index=True)
    match_id = Column(Integer, ForeignKey('matches.id'))
    set_number = Column(Integer, nullable=False)
    player1_games = Column(Integer, nullable=False)
    player2_games = Column(Integer, nullable=False)

    match = relationship('Match', back_populates='sets')

    __table_args__ = (
        UniqueConstraint('match_id', 'set_number'),
    )