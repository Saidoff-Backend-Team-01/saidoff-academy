from sqlalchemy.orm import Session


from app.models.sponsors import Sponsors



def get_sponsors(db: Session):
    return db.query(Sponsors).all()