from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100),  nullable=True)
    employmentStatus = Column(String(100), nullable=True)

    users = relationship("User", back_populates="review")
    users = relationship("User", back_populates="promo")