
import pygame
from config.settings import BG_COLOR

class GameRenderer:
    """ Renders the game state to the screen. """
    def __init__(self, screen, tilemap):

        self.screen = screen
        self.tilemap = tilemap
        self.bg_color = BG_COLOR

    def render_game(self, game_state):
        """ Renders the entire game state. """
        self._draw_background()
        self._draw_tilemap()
        self._draw_towers(game_state.towers)
        self._draw_enemies(game_state)
        self._draw_projectiles(game_state.projectiles)

    def _draw_background(self):
        """ Draws the background color. """
        self.screen.fill(self.bg_color)

    def _draw_tilemap(self):
        """ Draws the tilemap. """
        self.tilemap.draw(self.screen)

    def _draw_towers(self, towers):
        """ Draws all towers. """
        for tower in towers:
            tower.draw(self.screen)

    def _draw_enemies(self, game_state):
        """ Draws all enemies. """
        if game_state.enemy_manager:
            for enemy in game_state.enemy_manager.enemies:
                enemy.draw(self.screen)

    def _draw_projectiles(self, projectiles):
        """ Draws all projectiles. """
        for projectile in projectiles:
            if projectile:
                projectile.draw(self.screen)

    def draw_tower_ghost(self, tower_image, mouse_pos, tile_size, is_valid):
        """ Draws a ghost image of the tower at the mouse position. """
        mouse_x, mouse_y = mouse_pos
        tile_x = (mouse_x // tile_size) * tile_size + tile_size // 2
        tile_y = (mouse_y // tile_size) * tile_size + tile_size // 2

        ghost_size = (tower_image.get_width(), tower_image.get_height())

        if is_valid:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)

        # Create highlight overlay
        highlight = pygame.Surface(ghost_size)
        highlight.set_alpha(100)
        highlight.fill(color)

        # Draw position (centered on tile)
        position = (tile_x - ghost_size[0] // 2, tile_y - ghost_size[1] // 2)

        self.screen.blit(highlight, position)
        self.screen.blit(tower_image, position)

    def finalize_frame(self):
        """ Finalizes the frame by updating the display. """
        pygame.display.flip()
