""" This module contains configuration settings for the Slime Harvester game. """
from config.generate_wave_config import generate_wave_config

SCREEN_WIDTH = 1088
SCREEN_HEIGHT = 768
FPS = 60
BG_COLOR = (30, 30, 30)
MAP_NAME = "maps/map2.txt"
MAX_HEALTH = 100
TILE_SIZE = 32
START_MONEY = 50

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
            "damage":1, "range":800, "fire_rate":40, "price":30, "projectile_speed":3},
    "Tower2": {"projectile":"projectiles/projectile2.png",
            "damage":1, "range":100, "fire_rate":90, "price":80, "projectile_speed":5}
}

ENEMY_CONFIG = {
    "red_slime": {"name": "red_slime",
                "health": 1,
                "enemy_speed": 2,
                "enemy_image": "enemy_red.png",
                "next_type": 0},
    "blue_slime": {"name": "blue_slime",
                "health": 1,
                "enemy_speed": 2,
                "enemy_image": "enemy_blue.png",
                "next_type": "red_slime"},
    "green_slime": {"name": "green_slime",
                "health": 1,
                "enemy_speed": 3,
                "enemy_image": "enemy_green.png",
                "next_type": "blue_slime"},
    "pink_slime": {"name": "pink_slime",
                "health": 1,
                "enemy_speed": 5,
                "enemy_image": "enemy_pink.png",
                "next_type": "green_slime"},
    "black_slime": {"name": "black_slime",
                "health": 1,
                "enemy_speed": 5,
                "enemy_image": "enemy_black.png",
                "next_type": "pink_slime"},
    "boss_rainbow": {"name": "boss_rainbow",
                "health": 50,
                "enemy_speed": 1,
                "enemy_image": "enemy_boss_rainbow.png",
                "next_type": "pink_slime"},
    "boss_skull": {"name": "boss_skull",
                "health": 50,
                "enemy_speed": 1,
                "enemy_image": "enemy_boss_skull.png",
                "next_type": "boss_rainbow"}
}

WAVE_CONFIG = generate_wave_config(50)
