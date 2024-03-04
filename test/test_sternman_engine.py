import unittest
from engine.sternman_engine import SternmanEngine


class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):

        sternman_engine_false = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(sternman_engine_false.engine_should_be_serviced())

        sternman_engine_true = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(sternman_engine_true.engine_should_be_serviced())


if __name__ == '__main__':
    unittest.main()
