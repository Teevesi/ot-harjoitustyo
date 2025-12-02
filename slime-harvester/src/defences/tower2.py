import os
import pygame
from projectiles import Projectile
from settings import DIRECTION_VECTORS, TOWER_CONFIG
from load_image import load_image

class Tower2:
    def __init__(self, position):
        config = TOWER_CONFIG[self.__class__.__name__]
        self.position = position
        self.range = config["range"]
        self.damage = config["damage"]
        self.fire_rate = config["fire_rate"]
        self.last_shot_time = 0
        self.projectiles = []
        self.projectile_speed = config["projectile_speed"]
        self.price = config["price"]
        self.projectile_image = config["projectile"]

        self.image = load_image("defences/defence2.png")

    def can_shoot(self, frame):
        can_shoot = (frame - self.last_shot_time) >=  self.fire_rate
        if can_shoot:
            return True
        return False

    def shoot(self, frame):
        projectiles = []
        if self.can_shoot(frame):
            for dx, dy in DIRECTION_VECTORS.values():
                projectile = Projectile((self.position[0], self.position[1]), (dx, dy), self.projectile_speed, self.damage, self.range, self.projectile_image)
                projectiles.append(projectile)

            self.last_shot_time = frame
            return projectiles[:]

    def update(self, frame):

        for projectile in self.projectiles:
            projectile.update()

        self.projectiles = [p for p in self.projectiles if not p.has_exceeded_range()]

        new_projectiles = self.shoot(frame)
        if new_projectiles:
            self.projectiles.extend(new_projectiles)


    def draw(self, screen):
        width = self.image.get_width()
        height = self.image.get_height()
        screen.blit(self.image, (self.position[0] - width // 2, self.position[1] - height // 2))