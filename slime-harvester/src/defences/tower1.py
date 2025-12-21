# pylint: disable=duplicate-code
from dataclasses import dataclass
from projectiles.projectiles import Projectile, ProjectileStats
from config.settings import DIRECTION_VECTORS, TOWER_CONFIG
from config.load_image import load_image

@dataclass
class TowerStats:
    range: float
    damage: int
    fire_rate: int
    projectile_speed: float
    price: int
    projectile: str


class Tower1:
    """This class is for Tower1 defence. """
    def __init__(self, position):
        config = TOWER_CONFIG[self.__class__.__name__]
        self.position = position

        self.stats = TowerStats(
            range=config["range"],
            damage=config["damage"],
            fire_rate=config["fire_rate"],
            projectile_speed=config["projectile_speed"],
            price=config["price"],
            projectile=config["projectile"]
        )
        self.last_shot_time = 0
        self.projectiles = []
        self.direction = "left"
        self.projectile_image = self.stats.projectile
        self.image = load_image("defences/defence1.png")


    def can_shoot(self, frame):
        """ Checks if the tower can shoot based on its fire rate. """
        can_shoot = (frame - self.last_shot_time) >=  self.stats.fire_rate
        if can_shoot:
            return True
        return False

    def shoot(self, direction, frame):
        """ Shoots a projectile in the given direction if possible. """
        projectiles = []
        if self.can_shoot(frame):
            dx, dy = DIRECTION_VECTORS[direction]
            projectile = Projectile((self.position[0], self.position[1]), (dx, dy),
                                ProjectileStats(self.stats.projectile_speed, self.stats.damage,
                                                self.stats.range, self.stats.projectile))
            self.last_shot_time = frame
            projectiles.append(projectile)
            return projectiles
        return projectiles

    def update(self, frame):
        """ Updates the tower's projectiles. Add new projectiles if shooting. """
        for projectile in self.projectiles:
            projectile.update()

        self.projectiles = [p for p in self.projectiles if not p.has_exceeded_range()]

        self.shoot(self.direction, frame)


    def draw(self, screen):
        """ Draws the tower on the given screen. """
        width = self.image.get_width()
        height = self.image.get_height()
        screen.blit(self.image, (self.position[0] - width // 2, self.position[1] - height // 2))
