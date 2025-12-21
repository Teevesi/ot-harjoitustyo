# pylint: disable=no-member
import pygame
from config.settings import TILE_SIZE


class InputHandler:
    """ Handles user input events and tower placement logic. """
    def __init__(self, game_state, tower_dragging, ui):
        self.game_state = game_state
        self.tower_dragging = tower_dragging
        self.ui = ui

    def handle_events(self):
        """ Handles all user input events. """
        # Early exit if game over
        if self.game_state.is_game_over():
            self.game_state.running = False
            return

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state.running = False
                continue

            for button in self.ui.tower_buttons:
                button.handle_event(event, self.tower_dragging.start_dragging)

            if event.type == pygame.KEYDOWN:
                pass  # extend here if needed

            self._handle_tower_placement(event)

    def _handle_tower_placement(self, event):
        """ Handles tower placement. """
        if event.type != pygame.MOUSEBUTTONUP or event.button != 1:
            return

        if not self.tower_dragging.is_dragging():
            return

        mouse_x, mouse_y = pygame.mouse.get_pos()
        tile_x = mouse_x // TILE_SIZE
        tile_y = mouse_y // TILE_SIZE
        grid_x = tile_x * TILE_SIZE + TILE_SIZE // 2
        grid_y = tile_y * TILE_SIZE + TILE_SIZE // 2

        tower_type = self.tower_dragging.dragged_tower_type
        if tower_type and \
            self.game_state.can_place_tower_at(tile_x, tile_y, self.tower_dragging.tilemap):

            self.game_state.add_tower(tower_type, (grid_x, grid_y))

        self.tower_dragging.reset_dragging()
