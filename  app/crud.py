from sqlmodel import Session, select
from models import Item
from schemas import ItemCreate


def create_item(session: Session, data: ItemCreate, owner_id: int) -> Item:
    item = Item(
        title = data.title,
        description = data.descritption,
        price = data.price,
        owner_id = data.owner_id
    )
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_item(session: Session, item_id: int) -> Item | None:
    return session.get(Item, item_id)

def list_items(session:Session):
    return session.exec(select(Item)).all()