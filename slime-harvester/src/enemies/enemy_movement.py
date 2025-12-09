import math
import os
import pygame

#AI generoima alkaa
class Enemy:
    """ Represents an enemy that moves along a predefined path. """
    def __init__(self, path, enemy_speed):
        base_dir = os.path.dirname(__file__)
        self.path = path            # list of (x, y) points
        self.speed = enemy_speed
        # Start at the center of the first tile; first *target* is the second point
        if not path:
            raise ValueError("path must contain at least one point")

        self.x, self.y = path[0]    # start at first point (center)
        self.index = 1 if len(path) > 1 else 0  # current target index
        path = "..", "assets", "enemies", "enemy_red.png"
        self.image = pygame.image.load(os.path.join(base_dir, *path))
        self.rect = self.image.get_rect(center=(self.x, self.y))

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
