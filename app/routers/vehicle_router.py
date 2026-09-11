from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.database.database import get_db
from app.schemas.vehicle import Vehicle, VehicleCreate
from app.services.vehicle_service import create_vehicle, get_vehicles


router = APIRouter(prefix='/vehicles', tags=['vehicles'])


@router.post('/', response_model=Vehicle)
def add_vehicle(vehicle: VehicleCreate, db: Session = Depends(get_db)):
    return create_vehicle(db=db, vehicle=vehicle)


@router.get('/', response_model=list[Vehicle])
def read_vehicles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_vehicles(db, skip=skip, limit=limit)