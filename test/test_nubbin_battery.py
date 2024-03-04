import unittest
from datetime import datetime, timedelta
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        current_date = datetime(2024, 3, 1)
        last_service_date = datetime(2020, 2, 28)
        nubbin_battery = NubbinBattery(current_date, last_service_date)

        self.assertFalse(nubbin_battery.battery_should_be_serviced())

        future_date = current_date + timedelta(days=4 * 365 + 1)
        nubbin_battery.last_service_date = future_date
        self.assertTrue(nubbin_battery.battery_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
