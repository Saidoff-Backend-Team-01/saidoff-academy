from app.models.config import Config

from sqlalchemy.orm import Session



def get_config(db: Session):
    return db.query(Config).first()