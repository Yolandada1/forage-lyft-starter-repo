import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        willoughby_engine_low_mileage = WilloughbyEngine(current_mileage=50000, last_service_mileage=20000)
        self.assertFalse(willoughby_engine_low_mileage.engine_should_be_serviced())

        willoughby_engine_high_mileage = WilloughbyEngine(current_mileage=80000, last_service_mileage=20000)
        self.assertTrue(willoughby_engine_high_mileage.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
