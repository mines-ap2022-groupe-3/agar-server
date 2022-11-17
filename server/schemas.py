from pydantic import BaseModel


class PositionBase(BaseModel):
    xpos: int
    ypos: int
    game: str
    player: str


class Position(PositionBase):
    id: int

    class Config:
        orm_mode = True
