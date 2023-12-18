from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    count = Column(Integer)
    container_id = Column(Integer, ForeignKey('containers.id'))
    container = relationship("Container", back_populates="items")
    item_type = Column(String) 


class Container(Base):
    __tablename__ = 'containers'

    id = Column(Integer, primary_key=True)
    weight = Column(Float)
    container_type = Column(String)  

    items = relationship("Item", back_populates="container")
    ship_id = Column(Integer, ForeignKey('ships.id'))
    ship = relationship("Ship", back_populates="containers")


class Port(Base):
    __tablename__ = 'ports'

    id = Column(Integer, primary_key=True)
    latitude = Column(Float)
    longitude = Column(Float)

    ships = relationship("Ship", back_populates="current_port")


class Ship(Base):
    __tablename__ = 'ships'

    id = Column(Integer, primary_key=True)
    fuel = Column(Float)
    current_port_id = Column(Integer, ForeignKey('ports.id'))
    total_weight_capacity = Column(Float)
    max_containers = Column(Integer)
    max_heavy = Column(Integer)
    max_refrigerated = Column(Integer)
    max_liquid = Column(Integer)
    fuel_consumption_per_km = Column(Float)

    current_port = relationship("Port", back_populates="ships")
    containers = relationship("Container", back_populates="ship")
