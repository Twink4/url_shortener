from sqlalchemy import (
    Column,
    Integer,
    String
)

from src.core.database import Base


class UrlModel(Base):
    __tablename__ = "links"
    
    id = Column(String, primary_key=True, nullable=False, unique=True)
    full_link = Column(String, nullable=False)
    short_link = Column(String, nullable=False)