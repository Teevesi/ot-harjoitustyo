import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.player_stats import HealthBar, Currency


class TestHealthBar(unittest.TestCase):
    def setUp(self):
        self.health_bar = HealthBar(100)

    def test_initial_health(self):
        self.assertEqual(self.health_bar.current_health(), 100)
        self.assertEqual(self.health_bar.max_health, 100)

    def test_take_damage(self):
        self.health_bar.take_damage(30)
        self.assertEqual(self.health_bar.current_health(), 70)


class TestCurrency(unittest.TestCase):
    def setUp(self):
        self.currency = Currency(100)

    def test_initial_amount(self):
        self.assertEqual(self.currency.current_amount(), 100)

    def test_increase_currency(self):
        self.currency.increase(50)
        self.assertEqual(self.currency.current_amount(), 150)

    def test_decrease_currency_with_sufficient_amount(self):
        result = self.currency.decrease(30)
        self.assertTrue(result)
        self.assertEqual(self.currency.current_amount(), 70)

    def test_decrease_currency_with_insufficient_amount(self):
        result = self.currency.decrease(150)
        self.assertFalse(result)
        self.assertEqual(self.currency.current_amount(), 100)

    def test_decrease_exact_amount(self):
        result = self.currency.decrease(100)
        self.assertTrue(result)
        self.assertEqual(self.currency.current_amount(), 0)

if __name__ == '__main__':
    unittest.main()
