""" This module contains configuration settings for the Slime Harvester game. """

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
            "damage":1, "range":500, "fire_rate":60, "price":50, "projectile_speed":3},
    "Tower2": {"projectile":"projectiles/projectile2.png",
            "damage":1, "range":100, "fire_rate":60, "price":100, "projectile_speed":5}
}

ENEMY_CONFIG = {
    "red_slime": {"health": 1, "enemy_speed": 2, "enemy_image": "enemy_red.png", "next_type": 0},
    "blue_slime": {"health": 1, "enemy_speed": 2, "enemy_image": "enemy_blue.png", "next_type": "red_slime"}
}

WAVE_CONFIG = {
    1: {"enemy_count": 5, "spawn_interval": 60, "enemy_type": "red_slime"},
    2: {"enemy_count": 10, "spawn_interval": 50, "enemy_type": "blue_slime"},
    3: {"enemy_count": 15, "spawn_interval": 40, "enemy_type": "red_slime"},
    4: {"enemy_count": 20, "spawn_interval": 30, "enemy_type": "red_slime"},
    5: {"enemy_count": 25, "spawn_interval": 20, "enemy_type": "red_slime"},
    6: {"enemy_count": 30, "spawn_interval": 10, "enemy_type": "red_slime"},
    7: {"enemy_count": 35, "spawn_interval": 10, "enemy_type": "red_slime"},
    8: {"enemy_count": 40, "spawn_interval": 5, "enemy_type": "red_slime"},
    9: {"enemy_count": 100000000, "spawn_interval": 5, "enemy_type": "red_slime"}

}
