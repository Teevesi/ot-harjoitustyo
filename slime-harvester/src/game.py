# pylint: disable=no-member
import pygame
from tilemap import TileMap
from settings import FPS, BG_COLOR, MAP_NAME, ENEMY_SPEED, MAX_HEALTH, TILE_SIZE
from enemies.enemy_path import EnemyPath
from enemies.enemy_timing import EnemyTiming, Timer
from user_interface import UserInterface
from player_stats import HealthBar, Currency
from defences.tower1 import Tower1
from defences.tower2 import Tower2
from load_image import load_image

class Game:
    def __init__(self, screen_width, screen_height):
        # Jaa nämä eri paikkoihin ettei pylint valita
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
        self.currency = Currency(100)
        self.ui = UserInterface(self.hp_bar, self.currency)
        self.enemy_path = EnemyPath(MAP_NAME, TILE_SIZE)
        self.projectiles = []
        self.tower_manager = TowerManager(self.screen, self.timer, self.projectiles, self.ui)
        self.enemy_manager = EnemyManager(self.timer, self.enemy_path, self.screen, self.hp_bar)
        self.buttons = self.ui.tower_buttons
        self.tower_dragging = TowerDragging(self.screen, self.tilemap, self.tower_manager)

    def game_loop(self):

        while self.running:
            self.get_events()
            self.draw_base()

            self.update_enemies_and_towers()

            self.update_projectiles()

            self.check_collision()

            self.draw_ui()
            self.clock.tick(FPS)
            self.timer.update()

        pygame.quit()

    def draw_base(self):
        self.screen.fill(self.bg_color)
        self.tilemap.draw(self.screen)

    def draw_ui(self):

        self.tower_dragging.drag()
        self.ui.draw(self.screen)
        pygame.display.flip()

    def get_events(self):
        if self.check_game_over():
            self.running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            for button in self.buttons:
                button.handle_event(event, self.tower_dragging.start_dragging)

            if event.type == pygame.KEYDOWN:
                pass # Placeholder for future key events

            self.get_mouseup_events(event)

    def update_enemies_and_towers(self):
        self.enemy_manager.add_enemies()
        self.enemy_manager.update_enemies()
        self.tower_manager.update_towers()

    def update_projectiles(self):
        self.projectiles[:] = [p for p in self.projectiles if p and not p.has_exceeded_range()]
        for projectile in self.projectiles:
            if projectile:
                projectile.update()
                projectile.draw(self.screen)

    def check_collision(self):
        to_remove = []
        for projectile in self.projectiles:
            for enemy in self.enemy_manager.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    self.enemy_manager.remove(enemy)
                    to_remove.append(projectile)
                    self.currency.increase(1)
                    break
        for projectile in to_remove:
            if projectile in self.projectiles:
                self.projectiles.remove(projectile)

    def get_mouseup_events(self, event):
        if event.type != pygame.MOUSEBUTTONUP or event.button != 1:
            return

        if not self.tower_dragging.is_dragging():
            return

        def tile_is_occupied(grid_x, grid_y):
            for tower in self.tower_manager.towers:
                if (grid_x, grid_y) == tower.position:
                    return True
            return False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        grid_x = (mouse_x // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
        grid_y = (mouse_y // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2

        tower_type = self.tower_dragging.dragged_tower_type
        if not tower_type:
            self.tower_dragging.reset_dragging()
            return

        if (self.tilemap.tile_is_free(grid_x // TILE_SIZE, grid_y // TILE_SIZE)
            and not tile_is_occupied(grid_x, grid_y)):
            if tower_type == "Tower1":
                new_tower = Tower1((grid_x, grid_y))
            elif tower_type == "Tower2":
                new_tower = Tower2((grid_x, grid_y))
            else:
                new_tower = None
            if new_tower:
                self.tower_manager.add_tower(new_tower)

        self.tower_dragging.reset_dragging()

    def start_game(self):
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)


    def check_game_over(self):
        hp = self.hp_bar.current_health()
        if hp <= 0:
            return True
        return False


class TowerManager:
    def __init__(self, screen, timer, projectiles, ui):
        self.towers = []
        self.screen = screen
        self.timer = timer
        self.projectiles = projectiles
        self.ui = ui

    def add_tower(self, tower):
        if self.ui.currency_stat.current_amount() >= tower.stats.price:
            self.ui.currency_stat.decrease(tower.stats.price)
            self.towers.append(tower)

    def update_towers(self):
        for tower in self.towers:
            tower.draw(self.screen)
            new_projectiles = []
            if tower.can_shoot(self.timer.get_real_timer()):
                if tower.__class__.__name__ == "Tower1":
                    new_projectiles = tower.shoot("left", self.timer.get_real_timer())
                elif tower.__class__.__name__ == "Tower2":
                    new_projectiles = tower.shoot(self.timer.get_real_timer())
                if new_projectiles:
                    self.projectiles.extend(new_projectiles)
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

class TowerDragging:
    def __init__(self, screen, tilemap, tower_manager):
        self.dragging = False
        self.dragged_tower_type = None
        self.dragged_tower_image = None
        self.screen = screen
        self.tilemap = tilemap
        self.tower_manager = tower_manager

    def reset_dragging(self):
        self.dragging = False
        self.dragged_tower_type = None
        self.dragged_tower_image = None

    def start_dragging(self, tower_type):
        self.dragging = True
        self.dragged_tower_type = tower_type

        self.dragged_tower_image = None
        if tower_type == "Tower1":
            self.dragged_tower_image = load_image("defences/defence1.png")
        elif tower_type == "Tower2":
            self.dragged_tower_image = load_image("defences/defence2.png")

    def drag(self):
        if self.dragging and self.dragged_tower_image:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            tile_x = (mouse_x // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
            tile_y = (mouse_y // TILE_SIZE) * TILE_SIZE + TILE_SIZE // 2
            ghost_width = self.dragged_tower_image.get_width()
            ghost_height = self.dragged_tower_image.get_height()
            if self.tilemap.tile_is_free(tile_x // TILE_SIZE, tile_y // TILE_SIZE):
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)
            for tower in self.tower_manager.towers:
                if (tile_x, tile_y) == tower.position:
                    color = (255, 0, 0)
            highlight = pygame.Surface((ghost_width, ghost_height))
            highlight.set_alpha(100)
            highlight.fill(color)
            position = (tile_x - ghost_width // 2, tile_y - ghost_height // 2)
            self.screen.blit(highlight, position)
            self.screen.blit(self.dragged_tower_image, position)

    def is_dragging(self):
        return self.dragging
