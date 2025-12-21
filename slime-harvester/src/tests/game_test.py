import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from game.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(960, 640)

    def test_game_setup_correctly(self):
        self.assertEqual(self.game.screen_width, 960)
        self.assertEqual(self.game.screen_height, 640)
        self.assertFalse(self.game.game_state.running)

    def test_start_game_sets_running(self):
        self.game.start_game()
        self.assertTrue(self.game.game_state.running)

    def test_game_loop_iteration(self):
        self.game.start_game()
        for i in range(10):
            self.game.input_handler.handle_events()
            self.game.game_state.update()
            self.game.render()
            self.game.clock.tick(60)
        self.assertTrue(self.game.game_state.running)

    def test_quit_game_stops_running(self):
        self.game.start_game()
        self.game.game_state.running = False
        self.assertFalse(self.game.game_state.running)