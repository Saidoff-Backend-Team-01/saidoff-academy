from sqlalchemy.orm import Session


from app.models.company import Sponsor



def get_sponsors(db: Session):
    return db.query(Sponsor).all()