# pylint: disable=no-member
import pygame
from config.tilemap import TileMap
from config.settings import FPS, MAP_NAME, TILE_SIZE
from ui.user_interface import UserInterface
from game.game_state import GameState
from game.game_renderer import GameRenderer
from input.input_handler import InputHandler
from input.tower_dragging import TowerDragging

class Game:
    """ Main game class that initializes and runs the game loop. """
    def __init__(self, screen_width, screen_height):
        # Initialize pygame and display
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.display.set_caption("Slime Harvester")
        self.clock = pygame.time.Clock()

        self.game_state = GameState()
        self.tilemap = TileMap(MAP_NAME)
        self.renderer = GameRenderer(self.screen, self.tilemap)
        self.ui = UserInterface(self.game_state.hp_bar,
                                self.game_state.currency,
                                self.game_state.wave_manager)
        self.tower_dragging = TowerDragging(self.tilemap, self.game_state)
        self.input_handler = InputHandler(self.game_state, self.tower_dragging, self.ui)

    def game_loop(self):
        """ Runs the main game loop. """
        while self.game_state.running:
            self.input_handler.handle_events()

            self.game_state.update()

            self.render()

            self.clock.tick(FPS)

        pygame.quit()

    def render(self):
        """ Renders the current game state to the screen. """
        self.renderer.render_game(self.game_state)

        # Draw tower placement ghost if dragging
        if self.tower_dragging.is_dragging():
            mouse_pos = pygame.mouse.get_pos()
            is_valid = self.tower_dragging.is_placement_valid(mouse_pos, TILE_SIZE)
            self.renderer.draw_tower_ghost(
                self.tower_dragging.dragged_tower_image,
                mouse_pos,
                TILE_SIZE,
                is_valid
            )

        self.ui.draw(self.screen)

        self.renderer.finalize_frame()

    def start_game(self):
        """ Starts the game by initializing the game state. """
        self.game_state.start_game()
