from database import Base
from sqlalchemy import Column,Integer,String,Boolean,Text,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True)
    username=Column(String(20),unique=True)
    email=Column(String(20),unique=True)
    password=Column(Text,nullable=False)
    is_active=Column(Boolean,default=False)
    is_staff=Column(Boolean,default=False)
    orders=relationship('Order',back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"

class Order(Base):

    PIZZA_STATUS = (
        ('SMALL','small'),
        ('MEDIUM','medium'),
        ('LARGE','large'),
        ('EXTRA-LARGE','extra-large')
    )
    ORDER_STATUS = (
        ('PENDING','pending'),
        ('IN-TRANSIT','in-transit'),
        ('DELIVERED','delivered'),
    )

    __tablename__='orders'
    id=Column(Integer,primary_key=True)
    quantity=Column(Integer,nullable=False)
    order_status=Column(ChoiceType(choices=ORDER_STATUS),default='PENDING')
    pizza_status=Column(ChoiceType(choices=PIZZA_STATUS),default='SMALL')
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship('User',back_populates='orders')
  
    def __repr__(self):
        return f"<Order {self.id}>"