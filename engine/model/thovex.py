from car import Car
from engine.capulet_engine import CapuletEngine
from battery.nubbin_battery import NubbinBattery


class Thovex(Car, CapuletEngine, NubbinBattery):
    def needs_service(self):
        return self.battery_should_be_serviced() or \
             self.engine_should_be_serviced()
