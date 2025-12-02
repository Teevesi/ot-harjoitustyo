import os
import pygame
from settings import DIRECTION_VECTORS
from load_image import load_image


class Projectile:

    def __init__(self, position, direction, speed, damage, max_range, image):
        self.image = load_image(image)
        self.x, self.y = position
        self.start_x, self.start_y = position
        self.dx, self.dy = direction
        self.speed = speed
        self.damage = damage
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.max_range = max_range
        self.distance_traveled = 0

    def update(self):
        self.x += self.dx * self.speed
        self.y += self.dy * self.speed
        self.rect.center = (self.x, self.y)

        self.distance_traveled = ((self.x - self.start_x) ** 2 + (self.y - self.start_y) ** 2) ** 0.5


    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def has_exceeded_range(self):
        return self.distance_traveled >= self.max_range