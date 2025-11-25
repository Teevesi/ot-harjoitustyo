from projectiles import Projectile
import pygame, os

class Tower:
    def __init__(self, position):
        self.position = position
        self.range = 100
        self.damage = 1
        self.fire_rate = 60
        self.last_shot_time = 0
        self.projectiles = []
        self.projectile_speed = 3

    def can_shoot(self, frame):
        return (frame - self.last_shot_time) >=  self.fire_rate

    def shoot(self, direction, frame):
        if self.can_shoot(frame):
            new_projectile = Projectile(self.position[0], self.position[1], direction, self.projectile_speed, self.damage)
            self.last_shot_time = frame
            self.projectiles.append(new_projectile)
            return new_projectile

    def update(self, frame):
        self.shoot("left", frame)
        for projectile in self.projectiles:
            projectile.update()

    def draw(self, screen):
        base_dir = os.path.dirname(__file__)
        assets_dir = os.path.join(base_dir, "..", "assets", "defences")
        self.image = pygame.image.load(os.path.join(assets_dir, "defence1.png"))

        width = self.image.get_width()
        height = self.image.get_height()
        screen.blit(self.image, (self.position[0] - width // 2, self.position[1] - height // 2))