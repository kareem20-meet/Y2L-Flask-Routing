from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base




Base = declarative_base()
class Product(Base):
   __tablename__ = 'Product'
   ID = Column(Integer, primary_key=True)
   name = Column(String)
   price = Column(String)
   picture_link = Column(String)
   description = Column(String)


Base = declarative_base()
class Cart(Base):
   __tablename__ = 'Cart'
   productID = Column(Integer, primary_key=True)



