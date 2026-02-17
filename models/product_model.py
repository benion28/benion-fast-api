from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
import uuid
from helpers.database import Base


def generate_uuid():
    return str(uuid.uuid4())


class Product(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, default=generate_uuid)
    title = Column(String)
    price = Column(Numeric)
    creator_id = Column(String, ForeignKey("users.id"))

    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)

    creator = relationship("User")
