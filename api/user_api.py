from fastapi import APIRouter
from pydantic import BaseModel, constr
import re

from database.user_service import get_all_users_db, login_db, delete_user_db, registration_db

users_router = APIRouter(tags=["Управление юзерами"],
                         prefix="/user")

regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def mail_checker(email):
    if re.fullmatch(regex, email):
        return True
    return False
class User(BaseModel):
    user_name: str
    phone_number: str
    email: str
    password: constr(min_length=5, max_length=15)
    birthday: str | None = None
    city: str | None = None
@users_router.post("/registration")
async def register_user(user_model: User):
    data = dict(user_model)
    mail_validator = mail_checker(user_model.email)
    if mail_validator:
        result = registration_db(**data)
        return {"status": 1, "message" : "Добро пожаловать в AvtoSELL2"}
    return {"status": 0, "message": "неправильная формат email:("}




@users_router.post("/login")
async def login_user(identificator:str, password: str ):
    result = login_db(identificator=identificator,
                      password=password)
    return {"status": 1, "message": result}

@users_router.get("/get_all_users")
async def get_all_users():

    result = get_all_users_db()

    return {"status":1, "message":result }


@users_router.delete('/del_user')
async def del_user(user_id):
    result = delete_user_db(user_id)

    return {"status":1, "message":"вы удалили акк :|"}
