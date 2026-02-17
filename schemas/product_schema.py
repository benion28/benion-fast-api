from pydantic import BaseModel
from typing import Optional
from decimal import Decimal


class ProductBase(BaseModel):
    title: Optional[str]
    price: Optional[Decimal]


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: str
    creator_id: str

    class Config:
        orm_mode = True
