import pygame
from tilemap import TileMap
from settings import fps, bg_color, map_name, enemy_speed
from enemy_path import EnemyPath
from enemy_movement import Enemy
from enemy_timing import EnemyTiming, Timer


class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.display.set_caption("Slime Harvester")
        self.clock = pygame.time.Clock()
        self.bg_color = bg_color
        self.tilemap = TileMap(map_name)
        self.running = False
        self.enemy_path = EnemyPath(map_name, 32)
        self.enemies = []
        self.timer = Timer()
        self.enemy_timing = EnemyTiming()


    def game_loop(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill(self.bg_color)
            self.tilemap.draw(self.screen)

            for enemy in self.enemies:
                if enemy.update() == True:
                    self.enemies.remove(enemy)
                    continue
                enemy.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(fps)
            self.timer.update()

            if self.enemy_timing.can_spawn(self.timer.get_real_timer()) == True:
                new_enemy = self.enemy_timing.spawn_enemy(self.enemy_path, enemy_speed)
                self.enemies.append(new_enemy)


        pygame.quit()


    def start_game(self):
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)
