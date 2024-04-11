from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PromoBase(BaseModel):
    promoText: str
    amount: int


class PromoCreate(PromoBase):
    user_id: int

class PromoUpdate(BaseModel):
    username: [str] = None
    user_id: Optional[int] = None
    promoText: Optional[str] = None
    amount: Optional[int] = None


class Promo(PromoBase):
    id: int

    class ConfigDict:
        from_attributes = True