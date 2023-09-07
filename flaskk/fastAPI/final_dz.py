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

from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel, Field
from flask_wtf import CSRFProtect
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

import databases 
import sqlalchemy
from sqlalchemy import ForeignKey

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

items = sqlalchemy.Table("items", metadata, 
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
                        sqlalchemy.Column("name",sqlalchemy.String(32)), 
                        sqlalchemy.Column("description",sqlalchemy.String(32)), 
                        sqlalchemy.Column("price",sqlalchemy.Float()), )

orders = sqlalchemy.Table("orders", metadata, 
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
                        sqlalchemy.Column("user_id", sqlalchemy.Integer, ForeignKey(ss.User.user_id)),

                        )

users = sqlalchemy.Table("users", metadata, 
                        sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True), 
                        
                        )

@app.get("/items/", response_model=List[ss.Item])
async def get_items(): 
    query = items.select()
    return await database.fetch_all(query)

@app.get("/items/{item_id}", response_model=ss.Item) 
async def read_item(item_id:int): 
    query = items.select().where(items.c.id == item_id) 
    return await database.fetch_one(query)

@app.put("/items/{item_id}", response_model=ss.Item)
async def update_item(item_id:int, new_item:ss.ItemIn): 
    query = items.update().where(items.c.id == item_id).values(**new_item.dict())
    await database.execute(query)
    return{**new_item.dict(),"id":item_id}

@app.post("/items/", response_model=ss.Item)
async def create_user(item:ss.ItemIn): 
    query = items.insert().values(name=item.name, email=item.email) 
    last_record_id = await database.execute(query) 
    return{**item.dict(),"id":last_record_id}

@app.delete("/items/{item_id}")
async def delete_item(item_id:int, new_item:ItemIn): 
    query = items.update().where(items.c.id == item_id)
    await database.execute(query)
    return {'message': 'Item deleted'}





