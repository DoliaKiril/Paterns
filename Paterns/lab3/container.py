from abc import ABC, abstractmethod


class Container(ABC):
    def __init__(self, ID, weight):
        self.ID = ID
        self.weight = weight

    @abstractmethod
    def consumption(self):
        pass

    def equals(self, other):
        return (
            isinstance(other, Container) and
            self.ID == other.ID and
            self.weight == other.weight
        )


class BasicContainer(Container):
    def __init__(self, ID, weight):
        if weight <= 4000:
            super().__init__(ID, weight)
        else:
            raise ValueError("Контейнер занадто важкий<= 4000.")

    def consumption(self):
        return 2.50 * self.weight


class HeavyContainer(Container):
    def __init__(self, ID, weight):
        if weight > 4000:
            super().__init__(ID, weight)
        else:
            raise ValueError("Контейнер занадто легкий > 4000.")

    def consumption(self):
        return 4.00 * self.weight


class RefrigeratedContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        return 7.00 * self.weight


class LiquidContainer(HeavyContainer):
    def __init__(self, ID, weight):
        super().__init__(ID, weight)

    def consumption(self):
        return 5.00 * self.weight
