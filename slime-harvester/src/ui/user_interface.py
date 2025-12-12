
import pygame
from ui.tower_button import TowerButton
from load_image import load_image

class UserInterface:
    """ This class manages user interface elements like health/currency
    display and tower buttons.
    """
    def __init__(self, health_bar, currency, wave_manager):
        self.health_bar = health_bar
        self.currency_stat = currency
        self.wave_manager = wave_manager
        self.tower_buttons = [
            # TowerButton instances can be added here in the future
            TowerButton(load_image("defences/defence1.png"), (1028, 68), "Tower1"),
            TowerButton(load_image("defences/defence2.png"), (1028, 132), "Tower2")
        ]

    def health(self):
        """ Initializes and returns the health display surface. """
        font = pygame.font.SysFont(None, 30)
        hp = self.health_bar.current_health()
        health = font.render(f"Health: {hp}", 1, (20, 255, 0))
        return health

    def health_background(self):
        """ Initializes and returns the health background surface. """
        background = pygame.Surface((120, 25))
        background.set_alpha(180)
        background.fill((0, 0, 0))
        return background

    def currency(self):
        """ Initializes and returns the currency display surface. """
        font = pygame.font.SysFont(None, 30)
        currency_amount = self.currency_stat.current_amount()
        currency = font.render(f"Currency: {currency_amount}", 1, (255, 215, 0))
        return currency

    def currency_background(self):
        """ Initializes and returns the currency background surface. """
        background = pygame.Surface((150, 25))
        background.set_alpha(180)
        background.fill((0, 0, 0))
        return background
    
    def wave(self):
        """ Initialized and returns the wave display surface. """
        font = pygame.font.SysFont(None, 30)
        current_wave = self.wave_manager.current_wave
        if current_wave <= 8:
            wave = font.render(f"Wave: {current_wave}", 1, (155, 215, 0))
        else:
            wave = font.render(f"Wave: Endless", 1, (155, 215, 0))
        return wave
    
    def wave_background(self):
        background = pygame.Surface((150, 25))
        background.set_alpha(180)
        background.fill((0, 0, 0))
        return background

    def draw(self, screen):
        """ Draws the user interface elements onto the given screen. """
        screen.blit(self.health_background(), (7, 7))
        screen.blit(self.health(), (10, 10))
        screen.blit(self.currency_background(), (7, 37))
        screen.blit(self.currency(), (10, 40))
        screen.blit(self.wave_background(), (207, 7))
        screen.blit(self.wave(), (210, 10))
        for button in self.tower_buttons:
            button.draw(screen)
