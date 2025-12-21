import os
import pygame

from config.settings import TILE_SIZE

class TileMap:
    """ Class to manage and render the tile map. """
    def __init__(self, file_path):
        base_dir = os.path.dirname(__file__)
        dir1 = os.path.join(base_dir, "..")
        file_path = os.path.join(dir1, file_path)
        path  = "..", "assets", "tiles"
        full_path = os.path.join(base_dir, *path)
        # Load tile images
        self.tile_images = {
            '#': pygame.image.load(os.path.join(full_path, "rock.png")),
            '-': pygame.image.load(os.path.join(full_path, "path_horizontal.png")),
            '!': pygame.image.load(os.path.join(full_path, "path_vertical.png")),
            'I': pygame.image.load(os.path.join(full_path, "path_upleft.png")),
            'O': pygame.image.load(os.path.join(full_path, "path_upright.png")),
            'K': pygame.image.load(os.path.join(full_path, "path_downleft.png")),
            'L': pygame.image.load(os.path.join(full_path, "path_downright.png")),
            '.': pygame.image.load(os.path.join(full_path, "grass.png")),
            ',': pygame.image.load(os.path.join(full_path, "grass_bush.png")),
            'S': pygame.image.load(os.path.join(full_path, "spawn_portal.png")),
            'B': pygame.image.load(os.path.join(full_path, "border.png")),
            'Q': pygame.image.load(os.path.join(full_path, "ui_bg_tl.png")),
            'E': pygame.image.load(os.path.join(full_path, "ui_bg_tr.png")),
            'A': pygame.image.load(os.path.join(full_path, "ui_bg_ml.png")),
            'D': pygame.image.load(os.path.join(full_path, "ui_bg_mr.png")),
            'Z': pygame.image.load(os.path.join(full_path, "ui_bg_bl.png")),
            'C': pygame.image.load(os.path.join(full_path, "ui_bg_br.png")),
        }

        self.map_data = []
        with open(file_path, 'r', encoding="utf-8") as f:
            for line in f:
                self.map_data.append(list(line.strip()))

        # Preload images scaled to tile size
        for key in self.tile_images:
            self.tile_images[key] = pygame.transform.scale(
                self.tile_images[key], (TILE_SIZE, TILE_SIZE)
            )

    def draw(self, surface):
        """ Draws the tile map onto the given surface. """
        for row_index, row in enumerate(self.map_data):
            for col_index, tile_char in enumerate(row):
                tile = self.tile_images[tile_char]
                surface.blit(
                    tile,
                    (col_index * TILE_SIZE, row_index * TILE_SIZE)
                )

    def tile_is_free(self, tile_x, tile_y):
        """ Checks if the tile at (tile_x, tile_y) is free for tower placement. """
        if tile_y < 0 or tile_y >= len(self.map_data):
            return False
        if tile_x < 0 or tile_x >= len(self.map_data[0]):
            return False

        tile = self.map_data[tile_y][tile_x]
        if tile in ["#", ".", ","]:
            return True

        return False
