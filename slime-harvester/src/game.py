import pygame
from tilemap import TileMap
from settings import fps, bg_color, map_name, enemy_speed
from enemy_path import EnemyPath
from enemy_movement import Enemy


class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption("Slime Harvester")
        self.clock = pygame.time.Clock()
        self.bg_color = bg_color
        self.tilemap = TileMap(map_name)
        self.running = False
        self.enemy_path = EnemyPath(map_name, 32)
        self.enemies = [Enemy(self.enemy_path.path, enemy_speed)]


    def game_loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                

            self.screen.fill(self.bg_color)

            # Draw the tilemap
            self.tilemap.draw(self.screen)

            for enemy in self.enemies:
                enemy.update()
                enemy.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(fps)

        pygame.quit()


    def start_game(self):
        self.enemy_path.get_path(self.enemy_path.map_data)
        self.running = True
        self.game_loop()