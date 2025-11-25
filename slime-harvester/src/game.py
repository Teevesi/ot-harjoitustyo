# pylint: disable=no-member
import pygame
from tilemap import TileMap
from settings import FPS, BG_COLOR, MAP_NAME, ENEMY_SPEED, MAX_HEALTH, TILE_SIZE
from enemy_path import EnemyPath
from enemy_timing import EnemyTiming, Timer
from user_interface import UserInterface
from player_stats import HealthBar
from defences.tower1 import Tower

class Game:
    def __init__(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.screen_width = screen_width
        self.screen_height = screen_height
        pygame.display.set_caption("Slime Harvester")
        self.clock = pygame.time.Clock()
        self.bg_color = BG_COLOR
        self.tilemap = TileMap(MAP_NAME)
        self.running = False
        self.timer = Timer()
        self.hp_bar = HealthBar(MAX_HEALTH)
        self.ui = UserInterface(self.hp_bar)
        self.projectiles = []
        self.enemy_path = EnemyPath(MAP_NAME, TILE_SIZE)
        self.tower_manager = TowerManager(self.screen, self.timer, self.projectiles)
        self.enemy_manager = EnemyManager(self.timer, self.enemy_path, self.screen, self.hp_bar)

    def game_loop(self):

        while self.running:
            self.get_events()
            if self.check_game_over():
                self.running = False

            self.screen.fill(self.bg_color)
            self.tilemap.draw(self.screen)

            self.enemy_manager.add_enemies()
            self.enemy_manager.update_enemies()

            self.tower_manager.update_towers(self.timer.get_real_timer())

            for projectile in self.projectiles:
                if projectile:
                    projectile.update()
                    projectile.draw(self.screen)

            #check for collisions
            for projectile in self.projectiles:
                for enemy in self.enemy_manager.enemies:
                    if projectile.rect.colliderect(enemy.rect):
                        self.enemy_manager.remove(enemy)
                        self.projectiles.remove(projectile)

            self.ui.draw(self.screen)

            pygame.display.flip()
            self.clock.tick(FPS)
            self.timer.update()

        pygame.quit()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    grid_x = (mouse_x // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
                    grid_y = (mouse_y // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
                    new_tower = Tower((grid_x, grid_y))
                    self.tower_manager.add_tower(new_tower)

    def start_game(self):
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)

    def check_game_over(self):
        if self.hp_bar.current_health <= 0:
            return True
        return False

class TowerManager:
    def __init__(self, screen, timer, projectiles):
        self.towers = []
        self.screen = screen
        self.timer = timer
        self.projectiles = projectiles

    def add_tower(self, tower):
        self.towers.append(tower)

    def update_towers(self):
        for tower in self.towers:
            tower.draw(self.screen)
            if tower.can_shoot(self.timer.get_real_timer()):
                self.projectiles.append(tower.shoot("left", self.timer.get_real_timer()))
            tower.update(self.timer.get_real_timer())

class EnemyManager:
    def __init__(self, timer, enemy_path, screen, hp_bar):
        self.enemies = []
        self.enemy_timing = EnemyTiming()
        self.enemy_path = enemy_path
        self.timer = timer
        self.screen = screen
        self.hp_bar = hp_bar

    def add_enemies(self):
        if self.enemy_timing.can_spawn(self.timer.get_real_timer()) is True:
            new_enemy = self.enemy_timing.spawn_enemy(self.enemy_path, ENEMY_SPEED)
            self.enemies.append(new_enemy)

    def update_enemies(self):
        for enemy in self.enemies:
            if enemy.update() is True:
                self.enemies.remove(enemy)
                self.hp_bar.take_damage(1)
                continue
            enemy.draw(self.screen)

    def remove(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)
