from model import Base, Product


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def creatthread():
  engine = create_engine('sqlite:///database.db')
  Base.metadata.create_all(engine)
  DBSession = sessionmaker(bind=engine)
  session = DBSession()
  return session



def add_product(name, price, picture_link, description):
    session = creatthread()
    product_object = Product(
        name=name,
        price=price,
        picture_link=picture_link,
        description= escription)
    session.add(product_object)
    session.commit()

def edit_by_id(ID, picture_link):
   session = creatthread()
   product_object = session.query(
       Product).filter_by(
       ID=ID).first()
   product_object.picture_link = picture_link
   session.commit()

def delete_Product(their_ID):
   session = creatthread()
   session.query(Product).filter_by(
       ID=their_ID).delete()
   session.commit()



def query_all():
   session = creatthread()
   products = session.query(Product).all()
   return products


def query_by_ID(their_ID):
    session = creatthread()
    product = session.query(
    Product).filter_by(
    ID=their_ID).first()
    return product





def add_to_cart(productID):
    session = creatthread()
    cart_object = Cart(
    productID=productID)
    session.add(cart_object)
    session.commit()

def query_by_cartID():
    session = creatthread()
    cart_object = Cart(
    cartID=cartID)
    session.add(cart_object)
    session.commit()
