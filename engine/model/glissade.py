from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.spindler_battery import SpindlerBattery


class Glissade(Car, WilloughbyEngine, SpindlerBattery):
    def needs_service(self):
        return self.battery_should_be_serviced() or \
            self.engine_should_be_serviced()
