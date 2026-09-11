from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.schemas.customer import Customer, CustomerCreate
from app.services.customer_service import create_customer, get_customers


router = APIRouter(prefix='/customers', tags=['customers'])


@router.post('/', response_model=Customer)
def add_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return create_customer(db=db, customer=customer)


@router.post('/', response_model=List[Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_customers(db, skip=skip, limit=limit)