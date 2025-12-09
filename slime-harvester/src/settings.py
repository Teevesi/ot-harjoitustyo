""" This module contains configuration settings for the Slime Harvester game. """

SCREEN_WIDTH = 1088
SCREEN_HEIGHT = 768
FPS = 60
BG_COLOR = (30, 30, 30)
MAP_NAME = "maps/map2.txt"
ENEMY_SPEED = 4
MAX_HEALTH = 100
TILE_SIZE = 32

DIRECTION_VECTORS = {
    "up": (0, -1),
    "down": (0, 1),
    "left": (-1, 0),
    "right": (1, 0),
    "up_left": (-0.707, -0.707),
    "up_right": (0.707, -0.707),
    "down_left": (-0.707, 0.707),
    "down_right": (0.707, 0.707)
}


TOWER_CONFIG = {
    "Tower1": {"projectile":"projectiles/projectile1.png",
            "damage":1, "range":500, "fire_rate":60, "price":50, "projectile_speed":3},
    "Tower2": {"projectile":"projectiles/projectile2.png",
            "damage":1, "range":100, "fire_rate":60, "price":100, "projectile_speed":5}
}

WAVE_CONFIG = {
    1: {"enemy_count": 5, "spawn_delay": 120},
    2: {"enemy_count": 10, "spawn_delay": 100},
    3: {"enemy_count": 15, "spawn_delay": 80}
}
