from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class promos(Base):
    __tablename__ = "promos"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    promoText = Column(String(100), nullable=True)
    amount = Column(Integer, index=True, nullable=False, server_default='0.0')

    promo = relationship("Promo", back_populates="user")