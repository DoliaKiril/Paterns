import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Item, Container, Port, Ship


engine = create_engine('sqlite:///item.db')
Session = sessionmaker(bind=engine)
session = Session()

###

containers = session.query(Container).all()
containers_data = [{'ID': container.id, 'weight': container.weight, 'type': container.container_type}
                   for container in containers]

#
items = session.query(Item).all()
items_data = [{'id': item.id, 'weight': item.weight, 'count': item.count,
               'container_type': item.container.container_type, 'item_type': item.item_type}
              for item in items]


#
ports = session.query(Port).all()
ports_data = [{'ID': port.id, 'latitude': port.latitude, 'longitude': port.longitude}
              for port in ports]

#
ships = session.query(Ship).all()
ships_data = [{'ID': ship.id, 'fuel': ship.fuel, 'totalWeightCapacity': ship.total_weight_capacity,
               'maxContainers': ship.max_containers, 'maxHeavy': ship.max_heavy,
               'maxRefrigerated': ship.max_refrigerated, 'maxLiquid': ship.max_liquid,
               'fuelConsumptionPerKM': ship.fuel_consumption_per_km}
              for ship in ships]


data_to_export = {
    'containers': containers_data,
    'items': items_data,
    'ports': ports_data,
    'ships': ships_data
}

with open('dbinfo.json', 'w') as json_file:
    json.dump(data_to_export, json_file, indent=2)

print("Дані експортовано у dbinfo.json.")
