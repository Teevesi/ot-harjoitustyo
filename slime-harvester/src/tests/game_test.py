import unittest
from game import Game



class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game(960, 640)

    def test_game_setup_correctly(self):
        self.assertEqual(self.game.screen_width, 960)
        self.assertEqual(self.game.screen_height, 640)
        self.assertFalse(self.game.running)


    def test_start_game_sets_running(self):
        self.game.start_game()
        self.assertTrue(self.game.running)