from typing import List
from fastapi import FastAPI
from app.config.database import Base, SessionLocal, engine

from app.routers.company import router as company_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    prefix='/api/v1/'
)

app.include_router(company_router)