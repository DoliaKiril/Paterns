from containers import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship
import json

with open('data.json', 'r') as json_file:
    loaded_data = json.load(json_file)

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
