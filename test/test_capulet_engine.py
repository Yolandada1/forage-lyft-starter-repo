import unittest
from engine.capulet_engine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        capulet_engine_low_mileage = CapuletEngine(current_mileage=20000, last_service_mileage=5000)
        self.assertFalse(capulet_engine_low_mileage.engine_should_be_serviced())

        capulet_engine_high_mileage = CapuletEngine(current_mileage=40000, last_service_mileage=10000)
        self.assertTrue(capulet_engine_high_mileage.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
