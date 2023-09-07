from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from enum import Enum

db = SQLAlchemy()

# class Status(str, Enum):
#     CREATED = 'CREATED'
#     RECEIVED = 'RECEIVED'
#     IN_WORK = 'IN WORK'
#     PAID = 'PAID'
#     DELIVERED = 'DELIVERED'
#     CANCELLED = 'CANCELLED'

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False) 
    email = db.Column(db.String(120), unique=True, nullable=False) 
    password = db.Column(db.String(120), unique=False, nullable=False)

    def __init__(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self): 
        return f'User({self.name},{self.last_name},{self.email},{self.password})'

class Order(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    order_date = db.Column(db.DateTime, default = datetime.utcnow)
    # status = db.Column(Enum(Status), default=Status.CREATED)

    def __init__(self, name, user_id, item_id, order_date, status):
        self.name = name
        self.user_id = user_id
        self.item_id = item_id
        self.order_date = order_date
        self.status = status

    def __repr__(self): 
        return f'Order({self.user_id},{self.item_id},{self.order_date},{self.status})'
    
class Item(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(50), unique=False, nullable=False)
    price = db.Column(db.Float(), unique=False, nullable=False)

    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __repr__(self): 
        return f'Item({self.name},{self.description},{self.price})'