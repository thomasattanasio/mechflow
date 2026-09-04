from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.database.database import Base


class Customer(Base):
    __tablename__ = 'Customers'


    id = Column(Integer, primary_key=True, index=True)

    first_name = Column(String, nullable=False)

    last_name = Column(String, nullable=False)

    email = Column(String, unique=True, index=True)

    phone = Column(String, nullable=False)


    # Relationship: A customer can have multiple vehicles
    vehicles = relationship('Vehicles', back_populates='owner')