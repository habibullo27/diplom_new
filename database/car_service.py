from sqlalchemy.engine.reflection import cache

from database.models import *
from database import get_db
from database import get_db
from database.models import Car


def add_car_db(car_name,car_disc, car_price, user_id):
    db = next(get_db())

    new_car = Car(car_name=car_name,
                  car_disc=car_disc,
                  car_price=car_price,
                  user_id=user_id)
    db.add(new_car)
    db.commit()
    return new_car

def get_all_car_db():
    db = next(get_db())

    get_all_car = db.query(Car).all()

    return get_all_car

def delete_car_db(id):
    db = next(get_db())

    dell_car = db.query(Car).filter_by(id=id).first()

    if dell_car:
        db.delete(dell_car)
        db.commit()
    else:
        return {'message': 'Не успешно'}

