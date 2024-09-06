from sqlalchemy.orm import Session

from app.schemas.services import ServicesCreateSchema, ServicesListSchema
from app.models.our_services import OurServices


def get_services(slug: str, db: Session):
    return db.query(OurServices).filter(OurServices.slug == slug).first()


def create_services(db: Session, services_create: ServicesCreateSchema):
    db_services = OurServices(**services_create.dict())
    db.add(db_services)
    db.commit()
    db.refresh(db_services)
    return db_services


