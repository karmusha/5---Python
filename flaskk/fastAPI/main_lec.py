import logging
from fastapi import FastAPI, Request
from typing import Optional
from pydantic import BaseModel
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

# uvicorn flaskk.fastAPI.main_lec:app --reload

# POST запрос
# curl -X "POST" "http://127.0.0.1:8000/items/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\": \"Best Sale\", \"description\": \"The best of the best\", \"price\": 9.99, \"tax\": 0.99}"

# PUT запрос
# curl -X "PUT" "http://127.0.0.1:8000/items/23" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\": \"New Name\", \"description\": \"New description of the object\", \"price\": 7.25, \"tax\": 0.41}"

# DELETE запрос
# curl -X "DELETE" "http://127.0.0.1:8000/items/13" -H "accept: application/json"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
templates = Jinja2Templates(directory="flaskk/fastAPI/templates")

app = FastAPI()

class Item(BaseModel): 
    name: str 
    description: Optional[str] = None 
    price: float 
    tax: Optional[float] = None

# @app.get('/')
# async def root():
#     logger.info('Отработал GET запрос.')
#     return {'message':'Hello World!'}

@app.get('/', response_class=HTMLResponse)
async def read_root():
    return '<h1>Hello World</h1>'

@app.get("/message")
async def read_message():
    message = {"message": "Hello World"} 
    return JSONResponse(content=message, status_code=200)

@app.get('/items/{item_id}')
async def read_item(item_id: int, q: str = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}

@app.get("/users/{user_id}/orders/{order_id}")
async def read_data(user_id: int, order_id: int): 
    # обработка данных
    return {"user_id": user_id, "order_id": order_id}

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10): 
    return {"skip": skip,"limit": limit}

@app.get("/{name}", response_class=HTMLResponse)
async def read_item(request: Request, name: str): 
    print(request)
    return templates.TemplateResponse("item.html", {"request": request, "name": name})

@app.post('/items/')
async def create_item(item: Item):
    logger.info('Отработал POST запрос.')
    return item

@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item):
    logger.info(f'Отработал PUT запрос для item_id = {item_id}.')
    return {'item_id': item_id, 'item': item}

@app.delete('/items/{item_id}')
async def delete_item(item_id: int):
    logger.info(f'Отработал DELETE запрос для item_id = {item_id}.')
    return {'item_id': item_id}
