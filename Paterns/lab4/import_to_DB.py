from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Item, Container, Port, Ship

engine = create_engine('sqlite:///item.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

###

container1 = Container(weight=3500, container_type="Basic")
container2 = Container(weight=5500, container_type="Heavy")
container3 = Container(weight=4200, container_type="Refrigerated")

session.add_all([container1, container2, container3])
session.commit()
#
item1 = Item(weight=2.5, count=10, container_id=1, item_type="Basic")
item2 = Item(weight=3.0, count=8, container_id=2, item_type="Refrigerated")
item3 = Item(weight=2.0, count=15, container_id=3, item_type="Liquid")

session.add_all([item1, item2, item3])
session.commit()
#
port1 = Port(latitude=41.8781, longitude=-87.6298)
port2 = Port(latitude=37.7749, longitude=-122.4194)

session.add_all([port1, port2])
session.commit()
#
ship = Ship(fuel=1200, current_port=port1, total_weight_capacity=6000, max_containers=12,
            max_heavy=6, max_refrigerated=4, max_liquid=3, fuel_consumption_per_km=0.18)

session.add(ship)
session.commit()
#
print("Дані додано до бази даних.")
