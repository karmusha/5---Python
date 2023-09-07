from datetime import datetime
from pydantic import BaseModel, Field


class Item(BaseModel): 
    name: str = Field(title="Name", max_length=50)
    price: float = Field(title="Price", gt=0, le=1000000)
    description: str = Field(default=None, title="Description", max_length=1000) 
    tax: float = Field(0, title="Tax", ge=0, le=25)

class Order(BaseModel):
    user_id: int = Field(title="Price", gt=0, le=1000000)
    item_id: int = Field(title="Price", gt=0, le=1000000)
    order_date: datetime = Field(title="Price", default = datetime.utcnow)
    status: str = Field(title="Status", max_length=50)

class User(BaseModel): 
    name: str = Field(title="Name", max_length=50)
    last_name: str = Field(title="Last Name", max_length=50)
    email: str = Field(title="Last Name", max_length=50)
    password: str = Field(title="Last Name", max_length=50)
