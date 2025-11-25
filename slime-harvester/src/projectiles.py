import os
import pygame


class Projectile:

    def __init__(self, position, direction, speed, damage):
        base_dir = os.path.dirname(__file__)
        self.x = position[0]
        self.y = position[1]
        self.direction = direction
        self.speed = speed
        self.damage = damage
        image_path = os.path.join(base_dir, "assets", "projectiles", "projectile1.png")
        self.image = pygame.image.load(image_path)
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
