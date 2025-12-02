import pygame
from tower_button import TowerButton
from load_image import load_image

class UserInterface():
    def __init__(self, health_bar, currency):
        self.health_bar = health_bar
        self.currency_stat = currency
        self.tower_buttons = [
            # TowerButton instances can be added here in the future
            TowerButton(load_image("defences/defence1.png"), (1028, 68), "Tower1"),
            TowerButton(load_image("defences/defence2.png"), (1028, 132), "Tower2")
        ]

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

    def currency(self):
        font = pygame.font.SysFont(None, 30)
        currency_amount = self.currency_stat.current_amount()
        currency = font.render(f"Currency: {currency_amount}", 1, (255, 215, 0))
        return currency

    def currency_background(self):
        background = pygame.Surface((150, 25))
        background.set_alpha(180)
        background.fill((0, 0, 0))
        return background

    def draw(self, screen):
        screen.blit(self.health_background(), (7, 7))
        screen.blit(self.health(), (10, 10))
        screen.blit(self.currency_background(), (7, 37))
        screen.blit(self.currency(), (10, 40))
        for button in self.tower_buttons:
            button.draw(screen)
