from fastapi import FastAPI

from app.database.database import engine, Base
from app.routers import customer_router, vehicle_router


Base.metadata.create_all(bind=engine)


app = FastAPI(title='MechFlow API', description='Operational management system for mechanical workshops')


app.include_router(customer_router)
app.include_router(vehicle_router)


@app.get('/')
def read_root():
    return {'message': 'Welcome to MechFlow API. Documentation available at /docs'}