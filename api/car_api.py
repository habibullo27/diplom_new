from fastapi import FastAPI, APIRouter, UploadFile, File
from pydantic import BaseModel
from database import get_db
from database.models import Photo
import random, imghdr


from database.car_service import add_car_db, get_all_car_db, delete_car_db

car_router = APIRouter(tags=['Управление машинами'], prefix='/car')


class Car(BaseModel):
    car_name: str
    car_disc: str
    car_price: str
    user_id: int
@car_router.post('/add_car')
async def add_car(car_model: Car):
    data = dict(car_model)

    result = add_car_db(**data)

    return {'message':'Успешно добавили машину, ждите звонка:)'}

@car_router.get('/get_car')
async def get_car():
    result = get_all_car_db()
    return {'message':result}

@car_router.delete('/delete_car')
async def delete_car(id):
    del_car = delete_car_db(id)

    return {'massage':'Удаленоооо:('}


@car_router.post("/add_photoCAR")
async def add_photo2(photo_id: int, photo_file: UploadFile = File(...)):
    db = next(get_db())
    file_id = random.randint(1, 10000000000000)
    file_path = f"database/photos/photo_{file_id}_{photo_id}.jpg"

    with open(file_path, "wb") as photo_in_project:
        photo_to_save = await photo_file.read()
        photo_type = imghdr.what(None, photo_to_save)
        print(photo_type)
        photo_in_project.write(photo_to_save)

    new_photo = Photo(car_id=photo_id, filename=file_path, filepath=file_path)
    db.add(new_photo)
    db.commit()

    return {"status": 1, "message": "Фото вашего авто успешно загружено :) "}


@car_router.delete("/delete_photo")
async def delete_photo(photo_id: int):
    db = next(get_db())
    photo = db.query(Photo).filter_by(id=photo_id).first()
    if not photo:
        return {"status": 0, "message": "Фото не найдено"}

    db.delete(photo)
    db.commit()
    return {"status": 1, "message": "Фото успешно удалено из базы :)"}
