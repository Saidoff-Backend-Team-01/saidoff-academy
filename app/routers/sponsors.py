from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from app.config.database import get_db
from app.crud.sponsors import get_sponsors
from app.schemas.sponsor import SponsorModel

router = APIRouter(
    prefix="/company"
)

@router.get('/sponsors', response_model=list[SponsorModel])
def get_all_sonsors(db: Session = Depends(get_db)):
    sponsors = get_sponsors(db=db)

    return [SponsorModel(url=sponsor.url, image=sponsor.image).return_data() for sponsor in sponsors]