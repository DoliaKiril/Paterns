from typing import List
from container import Container
from port import Port


class Ship:
    def __init__(self, ID, fuel, currentPort, totalWeightCapacity, maxContainers, maxHeavy,
                 maxRefrigerated, maxLiquid, fuelConsumptionPerKM):
        self.ID = ID
        self.fuel = fuel
        self.currentPort = currentPort
        self.totalWeightCapacity = totalWeightCapacity
        self.maxContainers = maxContainers
        self.maxHeavy = maxHeavy
        self.maxRefrigerated = maxRefrigerated
        self.maxLiquid = maxLiquid
        self.fuelConsumptionPerKM = fuelConsumptionPerKM

    def getCurrentContainers(self):
        return []



current_containers = ship1.getCurrentContainers()
for container in current_containers:
    print(f"Контейнер {container.ID}, має тип: {container.type}")
