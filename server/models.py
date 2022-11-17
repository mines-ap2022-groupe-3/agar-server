from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from .db import Base

class Position(Base):
    __tablename__ = "positions"

    id = Column(Integer, primary_key=True, index=True)
    xpos = Column(Integer, index=True)
    ypos = Column(Integer, index=True)
    game = Column(String, index=True)
    player = Column(String, index=True)
