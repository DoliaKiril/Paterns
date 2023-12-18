from abc import ABC, abstractmethod


class IItem(ABC):
    def __init__(self, id: str, weight: float, count: int, container_type: str, item_type: str):
        self.id = id
        self.weight = weight
        self.count = count
        self.container_type = container_type
        self.item_type = item_type

    @staticmethod
    def check_type(id, weight, count, container_type=None, item_type=None):
        if item_type is None:
            return Item(id, weight, count, container_type, "Basic")
        
        elif item_type == "R":
            return RefrigeratedItem(id, weight, count, container_type, "Refrigerated")

        elif item_type == "L":
            return LiquidItem(id, weight, count, container_type, "Liquid")


class Item(IItem):
    def __init__(self, id, weight, count, container_type, item_type):
        super().__init__(id, weight, count, container_type, item_type)

    def getTotalWeight(self):
        return self.weight * self.count

class RefrigeratedItem(IItem):
    def __init__(self, id, weight, count, container_type, item_type):
        super().__init__(id, weight, count, container_type, item_type)

    def getTotalWeight(self):
        return self.weight * self.count


class LiquidItem(IItem):
    def __init__(self, id, weight, count, container_type, item_type):
        super().__init__(id, weight, count, container_type, item_type)

    def getTotalWeight(self):
        return self.weight * self.count
