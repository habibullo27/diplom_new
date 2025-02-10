from fastapi import FastAPI

from api.car_api import car_router
from api.user_api import users_router
from database import engine,Base
app = FastAPI(docs_url="/")
Base.metadata.create_all(bind=engine)
app.include_router(users_router)
app.include_router(car_router)

# uvicorn main:app --reload
