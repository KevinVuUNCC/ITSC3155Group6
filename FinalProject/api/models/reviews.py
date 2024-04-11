from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100),  nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    reviewText = Column(String(100), nullable=True)

    review = relationship("Review", back_populates="user")