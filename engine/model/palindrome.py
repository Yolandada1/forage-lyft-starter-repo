from car import Car
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery


class Palindrome(Car, SternmanEngine, SpindlerBattery):
    def needs_service(self):
        return self.battery_should_be_serviced() or \
            self.engine_should_be_serviced()
