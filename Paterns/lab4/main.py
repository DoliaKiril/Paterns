from models import Base, Item, Container, Ship, Port
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///item.db')
Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()

loaded_data = {
    'containers': [],
    'ports': [],
    'ship': None
}

all_containers = session.query(Container).all()
for container in all_containers:
    container_data = {
        'ID': container.id,
        'weight': container.weight,
        'type': container.container_type 
    }
    loaded_data['containers'].append(container_data)


all_ports = session.query(Port).all()
for port in all_ports:
    port_data = {
        'ID': port.id,
        'latitude': port.latitude,
        'longitude': port.longitude
    }
    loaded_data['ports'].append(port_data)

ship = session.query(Ship).first()
ship_data = {
    'ID': ship.id,
    'fuel': ship.fuel,
    'totalWeightCapacity': ship.total_weight_capacity,
    'maxContainers': ship.max_containers,
    'maxHeavy': ship.max_heavy,
    'maxRefrigerated': ship.max_refrigerated,
    'maxLiquid': ship.max_liquid,
    'fuelConsumptionPerKM': ship.fuel_consumption_per_km
}
loaded_data['ship'] = ship_data

###

for container_data in loaded_data['containers']:
    print(
        f"Контейнер ID {container_data['ID']} - Вага: {container_data['weight']} кг - Тип: {container_data['type']}")

for port_data in loaded_data['ports']:
    print(
        f"Порт ID {port_data['ID']} - Широта: {port_data['latitude']}, Довгота: {port_data['longitude']}")

ship_data = loaded_data['ship']
print("\nКорабель:")
print(f"ID: {ship_data['ID']}")
print(f"Паливо: {ship_data['fuel']} літрів")
print(f"Максимальне навантаження: {ship_data['totalWeightCapacity']} кг")
print(f"Максимальна кількість контейнерів: {ship_data['maxContainers']}")
print(f"Максимальна кількість важких контейнерів: {ship_data['maxHeavy']}")
print(f"Максимальна кількість морозильників: {ship_data['maxRefrigerated']}")
print(f"Максимальна кількість рідинних контейнерів: {ship_data['maxLiquid']}")
print(f"Споживання пального: {ship_data['fuelConsumptionPerKM']} на КМ")


