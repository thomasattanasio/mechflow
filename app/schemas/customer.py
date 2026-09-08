from pydantic import BaseModel, EmailStr
from typing import List, Optional


class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str


class CustomerCreate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int


    class Config:
        from_attributes = True