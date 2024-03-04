from abc import ABC, abstractmethod
from engine import Serviceable
from engine import Engine
from battery import Battery


class Car(ABC, Engine, Battery, Serviceable):

    @abstractmethod
    def needs_service(self):
        return self.battery_should_be_serviced() or \
            self.engine_should_be_serviced()
