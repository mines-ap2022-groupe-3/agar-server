from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .db import SessionLocal, engine

models.Base.metadata.create_all(engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/position", response_model=schemas.Position)
def create_position(position: schemas.PositionBase, db: Session = Depends(get_db)):
    return crud.create_position(db=db, position=position)


@app.get("/positions", response_model=list[schemas.Position])
def get_positions(game: str, db: Session = Depends(get_db)):
    positions = crud.get_positions(db, game)
    return positions