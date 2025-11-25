from game import Game

from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.start_game()
    game.game_loop()

if __name__ == "__main__":
    main()
