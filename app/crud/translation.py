
from sqlalchemy.orm import Session

from app.models.translation import Item, ItemTranslation


def get_item(db: Session, item_id: int, locale: str):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item:
        translation = db.query(ItemTranslation).filter(
            ItemTranslation.item_id == item_id,
            ItemTranslation.language_code == locale
        ).first()

        if translation:
            return {
                "name": translation.translated_name,
                "description": translation.translated_description
            }
        else:
            return {"name": item.name, "description": item.description}
    return None


def create_item(db: Session, name: str, description: str, translations: list):
    new_item = Item(name=name, description=description)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)

    for translation in translations:
        translated_item = ItemTranslation(
            item_id=new_item.id,
            language_code=translation["language_code"],
            translated_name=translation["name"],
            translated_description=translation["description"]
        )
        db.add(translated_item)

    db.commit()
    return new_item
