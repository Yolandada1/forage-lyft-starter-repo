from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def tire_should_be_serviced(self):
        pass
