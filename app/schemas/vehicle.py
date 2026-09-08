from pydantic import BaseModel


class VehicleBase(BaseModel):
    plate: str
    brand: str
    model: str


class VehicleCreate(VehicleBase):
    owner_id: int


class Vehicle(VehicleBase):
    id: int
    owner_id: int


    class Config:
        from_attributes = True