import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.game_state import GameState
from config.tilemap import TileMap
from config.settings import MAP_NAME


class TestGameState(unittest.TestCase):
    def setUp(self):
        self.game_state = GameState()
        self.tilemap = TileMap(MAP_NAME)

    def test_start_state(self):
        self.assertFalse(self.game_state.running)
        self.assertEqual(self.game_state.currency.current_amount(), 100)
        self.assertEqual(len(self.game_state.towers), 0)
        self.assertEqual(len(self.game_state.projectiles), 0)

    def test_start_game(self):
        self.game_state.start_game()
        self.assertTrue(self.game_state.running)

    def test_add_tower_with_enough_currency(self):
        initial_currency = self.game_state.currency.current_amount()
        add_tower = self.game_state.add_tower("Tower1", (100, 100))
        
        self.assertTrue(add_tower)
        self.assertEqual(len(self.game_state.towers), 1)
        self.assertLess(self.game_state.currency.current_amount(), initial_currency)

    def test_add_tower_with_not_enough_currency(self):
        self.game_state.currency.decrease(self.game_state.currency.current_amount())
        
        add_tower = self.game_state.add_tower("Tower1", (100, 100))
        
        self.assertFalse(add_tower)
        self.assertEqual(len(self.game_state.towers), 0)

    def test_game_over_when_health_zero(self):
        self.assertFalse(self.game_state.is_game_over())
        
        while self.game_state.hp_bar.current_health() > 0:
            self.game_state.hp_bar.take_damage(1)
        
        self.assertTrue(self.game_state.is_game_over())

if __name__ == '__main__':
    unittest.main()
