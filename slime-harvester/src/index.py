from game.game import Game

from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    """ Entry point for the Slime Harvester game. """
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.start_game()
    game.game_loop()

if __name__ == "__main__":
    main()
