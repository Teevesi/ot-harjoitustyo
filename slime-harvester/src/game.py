import pygame
from tilemap import TileMap
from settings import fps, bg_color, map_name, enemy_speed, max_health, tile_size
from enemy_path import EnemyPath
from enemy_movement import Enemy
from enemy_timing import EnemyTiming, Timer
from user_interface import UserInterface
from player_stats import HealthBar
from defences.tower1 import Tower
from projectiles import Projectile


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
        self.hp_bar = HealthBar(max_health)
        self.ui = UserInterface(self.hp_bar)
        self.towers = []
        self.projectiles = []


    def game_loop(self):

        while self.running:
            self.get_events()

            self.screen.fill(self.bg_color)
            self.tilemap.draw(self.screen)

            for enemy in self.enemies:
                if enemy.update() == True:
                    self.enemies.remove(enemy)
                    self.hp_bar.take_damage(1)
                    continue
                enemy.draw(self.screen)

            for tower in self.towers:
                tower.draw(self.screen)
                if tower.can_shoot(self.timer.get_real_timer()):
                    self.projectiles.append(tower.shoot("left", self.timer.get_real_timer()))
                tower.update(self.timer.get_real_timer())

            for projectile in self.projectiles:
                if projectile:
                    projectile.update()
                    projectile.draw(self.screen)

            #check for collisions
            for projectile in self.projectiles:
                for enemy in self.enemies:
                    if projectile.rect.colliderect(enemy.rect):
                        self.enemies.remove(enemy)
                        self.projectiles.remove(projectile)
                        

            self.ui.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(fps)
            self.timer.update()

            if self.enemy_timing.can_spawn(self.timer.get_real_timer()) == True:
                new_enemy = self.enemy_timing.spawn_enemy(self.enemy_path, enemy_speed)
                self.enemies.append(new_enemy)


        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:

                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = (mouse_x // tile_size) * tile_size + tile_size // 2
                    grid_y = (mouse_y // tile_size) * tile_size + tile_size // 2
                    new_tower = Tower((grid_x, grid_y))    
    
                    self.towers.append(new_tower)


    def start_game(self):
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)
