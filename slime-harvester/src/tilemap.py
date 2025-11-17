import os
import pygame

tile_size = 32


class TileMap:
    def __init__(self, file_path):
        base_dir = os.path.dirname(__file__)

        if not os.path.isabs(file_path):
            file_path = os.path.join(base_dir, file_path)

        self.tile_images = {
            '#': pygame.image.load(os.path.join(base_dir, "assets", "tiles", "rock.png")),
            '!': pygame.image.load(os.path.join(base_dir, "assets", "tiles", "path.png")),
            '.': pygame.image.load(os.path.join(base_dir, "assets", "tiles", "grass.png")),
            'S': pygame.image.load(os.path.join(base_dir, "assets", "tiles", "spawn_portal.png"))
        }

        self.map_data = []
        with open(file_path, 'r') as f:
            for line in f:
                self.map_data.append(list(line.strip()))

        # Preload images scaled to tile size
        for key in self.tile_images:
            self.tile_images[key] = pygame.transform.scale(
                self.tile_images[key], (tile_size, tile_size)
            )

    def draw(self, surface):
        for row_index, row in enumerate(self.map_data):
            for col_index, tile_char in enumerate(row):
                tile = self.tile_images[tile_char]
                surface.blit(
                    tile,
                    (col_index * tile_size, row_index * tile_size)
                )