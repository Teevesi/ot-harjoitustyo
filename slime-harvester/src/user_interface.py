import pygame

class UserInterface():
    def __init__(self, health_bar):
        self.health_bar = health_bar

    def health(self):
        font = pygame.font.SysFont(None, 30)
        hp = self.health_bar.current_health()
        health = font.render(f"Health: {hp}", 1, (20, 255, 0))
        return health

    def health_background(self):
        background = pygame.Surface((120, 25))
        background.set_alpha(180)
        background.fill((0, 0, 0))
        return background

    def draw(self, screen):
        screen.blit(self.health_background(), (7, 7))
        screen.blit(self.health(), (10, 10))
