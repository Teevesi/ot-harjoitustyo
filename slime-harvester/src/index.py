from game import Game

from settings import screen_width, screen_height

def main():
    game = Game(screen_width, screen_height)
    game.start_game()


if __name__ == "__main__":
    main()