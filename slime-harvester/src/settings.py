""" This module contains configuration settings for the Slime Harvester game. """
from generate_wave_config import generate_wave_config

SCREEN_WIDTH = 1088
SCREEN_HEIGHT = 768
FPS = 60
BG_COLOR = (30, 30, 30)
MAP_NAME = "maps/map2.txt"
ENEMY_SPEED = 2
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
            "damage":1, "range":500, "fire_rate":30, "price":30, "projectile_speed":3},
    "Tower2": {"projectile":"projectiles/projectile2.png",
            "damage":1, "range":100, "fire_rate":90, "price":80, "projectile_speed":5}
}

ENEMY_CONFIG = {
    "red_slime": {"health": 1,
                "enemy_speed": 2,
                "enemy_image": "enemy_red.png",
                "next_type": 0},
    "blue_slime": {"health": 1,
                "enemy_speed": 2,
                "enemy_image": "enemy_blue.png",
                "next_type": "red_slime"},
    "green_slime": {"health": 1,
                "enemy_speed": 3,
                "enemy_image": "enemy_green.png",
                "next_type": "blue_slime"},
    "pink_slime": {"health": 1,
                "enemy_speed": 5,
                "enemy_image": "enemy_pink.png",
                "next_type": "green_slime"}
}

WAVE_CONFIG = generate_wave_config(50)
