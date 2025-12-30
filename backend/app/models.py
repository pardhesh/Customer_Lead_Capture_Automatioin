from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base


class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    #entered by user
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    product = Column(String(255), nullable=True)
    message = Column(Text, nullable=False)
    #we will update these
    category = Column(String(50), nullable=True)
    status = Column(String(50), default="NEW")
    #time stamp (extra information)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
