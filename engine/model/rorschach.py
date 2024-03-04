from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery


class Rorschach(Car, WilloughbyEngine, NubbinBattery):
    def needs_service(self):
        return self.battery_should_be_serviced() or \
            self.engine_should_be_serviced()
