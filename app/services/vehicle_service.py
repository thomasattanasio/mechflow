from sqlalchemy.orm import Session
from app.models.vehicle import Vechicle
from app.schemas.vehicle import VehicleCreate


def create_vehicle(db: Session, vehicle: VehicleCreate):
    db_vehicle = Vechicle(
        plate=vehicle.plate,
        brand=vehicle.brand,
        model=vehicle.model,
        owner_id=vehicle.owner_id
    )


    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)


    return db_vehicle


def get_vehicles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Vechicle).offset(skip).limit(limit).all()