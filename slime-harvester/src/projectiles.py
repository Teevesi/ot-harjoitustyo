import pygame, os
import math

class Projectile:

    def __init__(self, x, y, direction, speed, damage):
        base_dir = os.path.dirname(__file__)
        self.x = x
        self.y = y
        self.direction = direction
        self.speed = speed
        self.damage = damage
        self.image = pygame.image.load(os.path.join(base_dir, "assets", "projectiles", "projectile1.png"))
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def update(self):
        if self.direction == "up":
            self.y -= self.speed
        elif self.direction == "down":
            self.y += self.speed
        elif self.direction == "left":
            self.x -= self.speed
        elif self.direction == "right":
            self.x += self.speed

        self.rect.center = (self.x, self.y)

    def draw(self, screen):
        screen.blit(self.image, self.rect)