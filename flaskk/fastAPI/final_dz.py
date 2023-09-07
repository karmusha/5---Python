"""
Необходимо создать базу данных для интернет-магазина. База данных должна состоять из трёх таблиц: товары, заказы и пользователи.
— Таблица «Товары» должна содержать информацию о доступных товарах, их описаниях и ценах.
— Таблица «Заказы» должна содержать информацию о заказах, сделанных пользователями.
— Таблица «Пользователи» должна содержать информацию о зарегистрированных пользователях магазина.

• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.

Создайте модели pydantic для получения новых данных и возврата существующих в БД для каждой из трёх таблиц.
Реализуйте CRUD операции для каждой из таблиц через создание маршрутов, REST API.

"""

from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from flask_wtf import CSRFProtect
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

import databases 
import sqlalchemy

from flaskk.fastAPI import models as ml
from flaskk.fastAPI import schemas as ss

DATABASE_URL="sqlite:///mydatabase.db"
database=databases.Database(DATABASE_URL)
metadata=sqlalchemy.MetaData()
engine=sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

app = FastAPI()

templates = Jinja2Templates(directory="flaskk/fastAPI/templates")


@app.on_event("startup")
async def startup(): 
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/items/")
async def get_items(): 
    return None

@app.get("/items/{item_id}")
async def get_item(item_id: int): 
    return None

@app.put("/items/{item_id}")
async def update_item(item_id: int): 
    return None

@app.post("/items/{item_id}")
async def create_item(item_id: int): 
    return None

@app.delete("/items/{item_id}")
async def delete_item(item_id: int): 
    return None





