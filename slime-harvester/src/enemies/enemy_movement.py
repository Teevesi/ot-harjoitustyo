import math
import os
import pygame

from config.settings import ENEMY_CONFIG

#AI generoima alkaa
class Enemy: # pylint: disable=too-many-instance-attributes
    """ Represents an enemy that moves along a predefined path. """
    def __init__(self, path, enemy_type):
        self.base_dir = os.path.dirname(__file__)
        self.path = path            # list of (x, y) points
        self.config = ENEMY_CONFIG
        self.speed = enemy_type["enemy_speed"]
        # Start at the center of the first tile; first *target* is the second point
        if not path:
            raise ValueError("path must contain at least one point")

        self.enemy_image = enemy_type["enemy_image"]
        self.x, self.y = path[0]    # start at first point (center)
        self.index = 1 if len(path) > 1 else 0  # current target index
        path = os.path.join("..", "assets", "enemies", self.enemy_image)
        full_path = os.path.join(self.base_dir, path)
        self.image = pygame.image.load(full_path)
        if enemy_type["name"] == "boss_rainbow":
            self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.enemy_type = enemy_type
        self.enemy_hp = enemy_type["health"]

    def update(self):
        """ Updates the enemy's position along its path.
            Returns True if the enemy has reached the end of the path. """
        # If at end of path → enemy finished
        if self.index >= len(self.path):
            return True   # done

        target_x, target_y = self.path[self.index]

        dx = target_x - self.x
        dy = target_y - self.y
        dist = math.hypot(dx, dy)

        # If we can reach or pass the target this frame, snap to center and advance
        if dist <= self.speed or dist == 0:
            self.x = target_x
            self.y = target_y
            self.index += 1
            # If we've reached the last point, signal finished next call
            return self.index >= len(self.path)

        # Move toward target proportionally so movement is smooth
        self.x += self.speed * dx / dist
        self.y += self.speed * dy / dist

        return False

    def draw(self, screen):
        """ Draws the enemy on the given screen. """
        self.rect.center = (self.x, self.y)
        screen.blit(self.image, self.rect)
#AI generoima loppuu
    def swap_enemy_type(self, new_enemy_type):
        """ Swaps the enemy type to new enemy type. """
        new_image = new_enemy_type["enemy_image"]
        path = os.path.join("..", "assets", "enemies", new_image)
        full_path = os.path.join(self.base_dir, path)
        self.image = pygame.image.load(full_path)
        self.enemy_type = new_enemy_type
        self.speed = new_enemy_type["enemy_speed"]
        self.enemy_hp = new_enemy_type["health"]
        self.reset_to_path()
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def reset_to_path(self):
        """ Resets the enemy's position to the closest point on the path. """
        min_dist = float('inf')
        closest_idx = 0

        for i, (px, py) in enumerate(self.path):
            dist = math.hypot(px - self.x, py - self.y)
            if dist < min_dist:
                min_dist = dist
                closest_idx = i

        self.x, self.y = self.path[closest_idx]
        self.index = closest_idx + 1 if closest_idx + 1 < len(self.path) else closest_idx

    def get_enemy_hp(self):
        """ Returns the enemy's health. """
        return self.enemy_hp

    def decrease_enemy_hp(self, amount):
        """ Decreases the enemy's health by the given amount. """
        self.enemy_hp -= amount
