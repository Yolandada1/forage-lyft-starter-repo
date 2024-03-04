import unittest
from datetime import datetime, timedelta
from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime(2024, 3, 1)
        last_service_date = datetime(2020, 2, 28)
        spindler_battery = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(spindler_battery.battery_should_be_serviced())

        future_date = current_date + timedelta(days=2 * 365 + 1)
        spindler_battery.last_service_date = future_date
        self.assertTrue(spindler_battery.battery_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
