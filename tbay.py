from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

engine = create_engine('postgresql://action:action@localhost:5432/tbay')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)
    start_time = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(Integer, ForeignKey(user.id), nullable=False)
    bids = relationship("Bid", backref="item")
    
    
class User(Base):
    __tablename__="users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    item = relationship("Item", backref="owner")
    bids = relationship ("Bid", backref="owner")
    
class Bid(Base):
    __tablename__="bids"
    
    id = Column(Integer, primary_key=True)
    bid_price = Column(Integer, nullable=False)
    owner_id = (Integer, ForeignKey(user.id), nullable=False)
    target_item = (Integer, ForeignKey(user.id), nullable=False)
    
Base.metadata.create_all(engine)