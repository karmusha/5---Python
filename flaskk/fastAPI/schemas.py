from datetime import datetime
from pydantic import BaseModel, Field
from sqlalchemy.orm import Mapped, mapped_column


class Item(BaseModel): 
    id: Mapped[int] = mapped_column(primary_key=True)
    name: str = Field(title="Name", max_length=50)
    description: str = Field(default=None, title="Description", max_length=1000) 
    price: float = Field(title="Price", gt=0, le=1000000)

class Order(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: int = Field(title="User_Id", g=0)
    item_id: int = Field(title="Item_Id", gt=0)
    order_date: datetime = Field(title="Price", default = datetime.utcnow)
    status: str = Field(title="Status", max_length=50)

class User(BaseModel):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: str = Field(title="Name", max_length=50)
    last_name: str = Field(title="Last Name", max_length=50)
    email: str = Field(title="Last Name", max_length=50)
    password: str = Field(title="Last Name", max_length=50)

class ItemIn(BaseModel):
    name: str = Field(title="Name", max_length=50)
    description: str = Field(default=None, title="Description", max_length=1000) 
    price: float = Field(title="Price", gt=0, le=1000000)
