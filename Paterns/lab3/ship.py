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


port1 = Port(1, 40.7128, 74.0060)
ship1 = Ship(1, 1000, port1, 5000, 10, 5, 3, 2, 0.2)


current_containers = ship1.getCurrentContainers()
for container in current_containers:
    print(f"Container {container.ID}: Type - {container.type}")
