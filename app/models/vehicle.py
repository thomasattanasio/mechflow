from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.database import Base


class Vechicle(Base):
    __tablename__ = 'Vehicles'


    id = Column(Integer, primary_key=True, index=True)

    plate = Column(String, unique=True, index=True, nullable=False)

    brand = Column(String, nullable=False)

    model = Column(String, nullable=False)

    owner_id = Column(Integer, ForeignKey('Customers.id'))


    # Relationship: A vehicle belongs only to one customer
    owner = relationship('Customer', back_populates='vehicles')