from sqlalchemy import (Column, String, Integer, DateTime, ForeignKey)
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    phone_number = Column(String, unique=True)
    email = Column(String, unique=True)
    city = Column(String, nullable=True)
    password = Column(String)
    birthday = Column(String, nullable=True)
    reg_date = Column(DateTime, default=datetime.now())

class Car(Base):
    __tablename__ = 'cars'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    car_name = Column(String)
    car_disc = Column(String)
    car_price = Column(Integer)
    users_fk = relationship(User, lazy="subquery")

class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    car_id = Column(Integer, ForeignKey("cars.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    filename = Column(String, unique=True, nullable=False)
    filepath = Column(String, nullable=False)
    size = Column(Integer)
    file_type = Column(String)
    uploaded_at = Column(DateTime, default=datetime.now)
    users_fk = relationship(User, lazy="subquery")
    car_fk = relationship(Car, lazy="subquery")
