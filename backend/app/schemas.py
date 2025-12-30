from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class LeadCreate(BaseModel):
    name: str
    email: EmailStr
    product: Optional[str] = None
    message: str


class LeadResponse(BaseModel):
    id: int
    name: str
    email: str
    product: Optional[str]
    message: str
    category: Optional[str]
    status: str
    created_at: datetime

    class Config:
        orm_mode = True
