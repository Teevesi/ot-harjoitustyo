"""Tower dragging state management (logic only).

This module keeps drag/drop state for tower placement. It loads the tower
images when dragging starts but avoids any rendering.
"""

from load_image import load_image


class TowerDragging:
    """Manages tower drag and drop state (no rendering)."""

    def __init__(self, tilemap, game_state):
        self.dragging = False
        self.dragged_tower_type = None
        self.dragged_tower_image = None
        self.tilemap = tilemap
        self.game_state = game_state

    def reset_dragging(self):
        self.dragging = False
        self.dragged_tower_type = None
        self.dragged_tower_image = None

    def start_dragging(self, tower_type):
        """Begin dragging a tower of the given type and load its image."""
        self.dragging = True
        self.dragged_tower_type = tower_type

        self.dragged_tower_image = None
        if tower_type == "Tower1":
            self.dragged_tower_image = load_image("defences/defence1.png")
        elif tower_type == "Tower2":
            self.dragged_tower_image = load_image("defences/defence2.png")

    def is_placement_valid(self, mouse_pos, tile_size):
        mouse_x, mouse_y = mouse_pos
        tile_x = mouse_x // tile_size
        tile_y = mouse_y // tile_size

        return self.game_state.can_place_tower_at(tile_x, tile_y, self.tilemap)

    def is_dragging(self):
        return self.dragging and self.dragged_tower_image is not None
