
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from database import get_session
from crud import create_item, get_item, list_items
from schemas import ItemCreate, ItemRead
from dependencies import get_current_user

router = APIRouter(prefix="/items",tags=["items"])


@router.get("/", response_model=list[ItemRead])
def get_all_items(
        session:Session = Depends(get_session),
        user = Depends(get_current_user)
):
    return list_items(session)


@router.post("/{item_id}",response_model=ItemRead)
def create_item(item_id: int,
                sessions:Session = Depends(get_session),
                user = Depends(get_current_user)
                ):
    result = get_item(sessions, item_id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return result