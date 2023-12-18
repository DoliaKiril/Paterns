import unittest
from unittest.mock import patch
from container import BasicContainer, HeavyContainer, RefrigeratedContainer, LiquidContainer
from port import Port
from ship import Ship


class TestContainers(unittest.TestCase):
    def test_basic(self):
        basic_container = BasicContainer(1, 3000)
        self.assertEqual(basic_container.consumption(), 2.50 * 3000)

    def test_heavy(self):
        heavy_container = HeavyContainer(2, 5000)
        self.assertEqual(heavy_container.consumption(), 4.00 * 5000)

    def test_refrigerated(self):
        refrigerated_container = RefrigeratedContainer(3, 6000)
        self.assertEqual(refrigerated_container.consumption(), 7.00 * 6000)

    def test_liquid(self):
        liquid_container = LiquidContainer(4, 7000)
        self.assertEqual(liquid_container.consumption(), 5.00 * 7000)


class TestPort(unittest.TestCase):
    def test_get_distance_between_ports(self):
        port1 = Port(1, 40.7128, 74.0060)
        port2 = Port(2, 34.0522, 118.2437)
        distance = port1.getDistance(port2)
        expected_distance = 3935.7516
        self.assertAlmostEqual(distance, expected_distance, places=2)

if __name__ == '__main__':
    unittest.main()
