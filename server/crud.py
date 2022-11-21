from sqlalchemy.orm import Session

from . import models, schemas


def get_positions(db: Session, game: str):
    return db.query(models.Position).where(models.Position.game == game).all()

def get_position_for_player(db: Session, game: str, player: str):
    return db.query(models.Position).where(models.Position.game == game, models.Position.player == player).one_or_none()

def create_position(db: Session, position: schemas.Position):
    current_position = get_position_for_player(db, position.game, position.player)

    if current_position is None:
        current_position = models.Position(
            xpos=position.xpos,
            ypos=position.ypos,
            game=position.game,
            player=position.player,
        )
    else:
        current_position.xpos = position.xpos
        current_position.ypos = position.ypos

    db.add(current_position)
    db.commit()
    db.refresh(current_position)
    return current_position
