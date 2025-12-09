"""Game renderer - handles all visual rendering without game logic.

This module contains the GameRenderer class which is responsible for
drawing all game elements to the screen. It reads from GameState but
doesn't modify it.
"""

import pygame
from settings import BG_COLOR


class GameRenderer:
    """Handles all game rendering (world, entities, effects).
    
    This class is responsible for drawing the game world including
    tiles, towers, enemies, and projectiles. It reads from GameState
    but never modifies it.
    
    Attributes:
        screen: pygame screen surface to draw on
        tilemap: TileMap instance for drawing the game map
    """

    def __init__(self, screen, tilemap):
        """Initialize the renderer.
        
        Args:
            screen: pygame screen surface
            tilemap: TileMap instance
        """
        self.screen = screen
        self.tilemap = tilemap
        self.bg_color = BG_COLOR

    def render_game(self, game_state):
        """Render the entire game scene.
        
        Args:
            game_state: GameState instance to read from
        """
        self._draw_background()
        self._draw_tilemap()
        self._draw_towers(game_state.towers)
        self._draw_enemies(game_state)
        self._draw_projectiles(game_state.projectiles)

    def _draw_background(self):
        """Draw the background color."""
        self.screen.fill(self.bg_color)

    def _draw_tilemap(self):
        """Draw the game map."""
        self.tilemap.draw(self.screen)

    def _draw_towers(self, towers):
        """Draw all towers.
        
        Args:
            towers: List of tower instances
        """
        for tower in towers:
            tower.draw(self.screen)

    def _draw_enemies(self, game_state):
        """Draw all enemies.
        
        Args:
            game_state: GameState instance to get enemies from
        """
        if game_state.enemy_manager:
            for enemy in game_state.enemy_manager.enemies:
                enemy.draw(self.screen)

    def _draw_projectiles(self, projectiles):
        """Draw all projectiles.
        
        Args:
            projectiles: List of projectile instances
        """
        for projectile in projectiles:
            if projectile:
                projectile.draw(self.screen)

    def draw_tower_ghost(self, tower_image, mouse_pos, tile_size, tilemap, towers, is_valid):
        """Draw a ghost preview of tower placement.
        
        Args:
            tower_image: pygame Surface of tower image
            mouse_pos: Tuple (x, y) of mouse position
            tile_size: Size of tiles in pixels
            tilemap: TileMap instance to check tile validity
            towers: List of existing towers to check overlap
            is_valid: Whether the placement is valid
        """
        mouse_x, mouse_y = mouse_pos
        tile_x = (mouse_x // tile_size) * tile_size + tile_size // 2
        tile_y = (mouse_y // tile_size) * tile_size + tile_size // 2
        
        ghost_width = tower_image.get_width()
        ghost_height = tower_image.get_height()
        
        # Determine color based on validity
        if is_valid:
            color = (0, 255, 0)
        else:
            color = (255, 0, 0)
        
        # Create highlight overlay
        highlight = pygame.Surface((ghost_width, ghost_height))
        highlight.set_alpha(100)
        highlight.fill(color)
        
        # Draw position (centered on tile)
        position = (tile_x - ghost_width // 2, tile_y - ghost_height // 2)
        
        self.screen.blit(highlight, position)
        self.screen.blit(tower_image, position)

    def finalize_frame(self):
        """Flip the display to show the rendered frame."""
        pygame.display.flip()
