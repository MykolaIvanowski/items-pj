from pydentic import BaseModel

class ItemCreate(BaseModel):
    title: str
    description: str
    price: float


class ItemRead(BaseModel):
    id: int
    tile: str
    description: str
    price: float
    owner_id: int


    class Config:
        orm_mode = True