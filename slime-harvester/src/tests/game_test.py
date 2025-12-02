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

    def test_game_loop_runs(self):
        self.game.start_game()
        for _ in range(10):
            self.game.get_events()
            self.game.draw_base()
            self.game.update_enemies_and_towers()
            self.game.update_projectiles()
            self.game.check_collision()
            self.game.draw_ui()
            self.game.clock.tick(60)
            self.game.timer.update()
        self.assertTrue(self.game.running)

    def test_quit_game_stops_running(self):
        self.game.start_game()
        self.game.running = False
        self.assertFalse(self.game.running)