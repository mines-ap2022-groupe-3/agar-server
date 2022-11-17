from sqlalchemy.orm import Session

from . import models, schemas


def get_positions(db: Session):
    return db.query(models.Position).all()


def create_position(db: Session, position: schemas.Position):
    db_position = models.Position(
        xpos=position.xpos,
        ypos=position.ypos,
        game=position.game,
        player=position.player,
    )
    db.add(db_position)
    db.commit()
    db.refresh(db_position)
    return db_position
