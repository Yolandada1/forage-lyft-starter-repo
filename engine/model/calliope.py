from car import Car
from engine.capulet_engine import CapuletEngine
from battery.spindler_battery import SpindlerBattery


class Calliope(Car, CapuletEngine, SpindlerBattery):
    def needs_service(self):
        return self.battery_should_be_serviced() or \
            self.engine_should_be_serviced()
