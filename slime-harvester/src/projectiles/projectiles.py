from dataclasses import dataclass
from config.load_image import load_image

@dataclass
class ProjectileStats:
    speed: float
    damage: int
    max_range: float
    image_path: str


class Projectile:
    """ Class to manage projectile behavior. """
    def __init__(self, position, direction, stats: ProjectileStats):
        self.image = load_image(stats.image_path)
        self.pos = (position[0], position[1])
        self.start_pos = (position[0], position[1])
        self.dx, self.dy = direction

        self.stats = stats
        self.rect = self.image.get_rect(center=self.pos)
        self.distance_traveled = 0

    def update(self):
        """ Update the projectile's position and distance traveled. """
        self.pos = (self.pos[0] + self.dx * self.stats.speed,
                    self.pos[1] + self.dy * self.stats.speed)
        self.rect.center = self.pos

        self.distance_traveled = ((self.pos[0] - self.start_pos[0]) ** 2 +
                                (self.pos[1] - self.start_pos[1]) ** 2) ** 0.5

    def draw(self, screen):
        """ Draws the projectile on the given screen. """
        screen.blit(self.image, self.rect)

    def has_exceeded_range(self):
        """ Checks if the projectile has exceeded its maximum range. """
        return self.distance_traveled >= self.stats.max_range
