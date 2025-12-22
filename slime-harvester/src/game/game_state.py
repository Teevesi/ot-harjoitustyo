
from config.settings import MAP_NAME, MAX_HEALTH, TILE_SIZE, START_MONEY
from enemies.enemy_path import EnemyPath
from enemies.enemy_timing import Timer
from enemies.enemy_manager import EnemyManager
from enemies.wave_manager import WaveManager
from game.player_stats import HealthBar, Currency
from defences.tower1 import Tower1
from defences.tower2 import Tower2


class GameState: # pylint: disable=too-many-instance-attributes
    """ This class manages the overall game state. """
    def __init__(self):
        self.timer = Timer()
        self.hp_bar = HealthBar(MAX_HEALTH)
        self.currency = Currency(START_MONEY)
        self.enemy_path = EnemyPath(MAP_NAME, TILE_SIZE)
        self.projectiles = []
        self.towers = []
        self.running = False

        self.enemy_manager = EnemyManager(
            self.timer,
            self.enemy_path,
            self.hp_bar
        )

        self.wave_manager = WaveManager(self.enemy_manager)

        self.selected_tower_type = None

    def start_game(self):
        """ Starts the game by setting running to True and initializing the enemy path. """
        self.running = True
        self.enemy_path.get_path(self.enemy_path.map_data)

    def is_game_over(self):
        """ Check if the game is over (health <= 0). """
        return self.hp_bar.current_health() <= 0

    def update(self):
        """ Update the game state. """
        if self.enemy_manager:
            # self.enemy_manager.add_enemies()
            self.wave_manager.spawn_wave()
            self.enemy_manager.update_enemies()

        self._update_towers()
        self._update_projectiles()
        self._check_collisions()
        self.timer.update()

    def _update_towers(self):
        """ Update all towers and handle shooting. """
        for tower in self.towers:
            new_projectiles = []
            if tower.can_shoot(self.timer.get_real_timer()):
                if tower.__class__.__name__ == "Tower1":
                    new_projectiles = tower.shoot("left", self.timer.get_real_timer())
                elif tower.__class__.__name__ == "Tower2":
                    new_projectiles = tower.shoot(self.timer.get_real_timer())
                if new_projectiles:
                    self.projectiles.extend(new_projectiles)
            tower.update(self.timer.get_real_timer())

    def _update_projectiles(self):
        """ Update all projectiles and remove those that exceeded their range. """
        self.projectiles[:] = [
            p for p in self.projectiles
            if p and not p.has_exceeded_range()
        ]

        for projectile in self.projectiles:
            if projectile:
                projectile.update()

    def _check_collisions(self):
        """ Check for collisions between projectiles and enemies. """
        to_remove = []

        if not self.enemy_manager:
            return

        for projectile in self.projectiles:
            for enemy in self.enemy_manager.enemies:
                if projectile.rect.colliderect(enemy.rect):
                    self.enemy_manager.get_enemy_hit_action(enemy)
                    to_remove.append(projectile)
                    currency_multiplier = max(1 - self.wave_manager.current_wave / 50, 0.1)
                    self.currency.increase(currency_multiplier)
                    break

        # Remove collided projectiles
        for projectile in to_remove:
            if projectile in self.projectiles:
                self.projectiles.remove(projectile)

    def add_tower(self, tower_type, position):
        """ Adds a tower of the specified type at the given position if affordable. """
        new_tower = None
        if tower_type == "Tower1":
            new_tower = Tower1(position)
        elif tower_type == "Tower2":
            new_tower = Tower2(position)

        if not new_tower:
            return False

        # Check if player can afford it
        if self.currency.current_amount() >= new_tower.stats.price:
            self.currency.decrease(new_tower.stats.price)
            self.towers.append(new_tower)
            return True

        return False

    def can_place_tower_at(self, tile_x, tile_y, tilemap):
        """ Check if a tower can be placed at the given tile coordinates. """
        # Check if tile is free
        if not tilemap.tile_is_free(tile_x, tile_y):
            return False

        # Check if another tower is already at this position
        grid_x = tile_x * TILE_SIZE + TILE_SIZE // 2
        grid_y = tile_y * TILE_SIZE + TILE_SIZE // 2

        for tower in self.towers:
            if tower.position == (grid_x, grid_y):
                return False

        return True

    def select_tower(self, tower_type):
        """ Select a tower type for placement. """
        self.selected_tower_type = tower_type

    def clear_tower_selection(self):
        """ Clear the current tower selection. """
        self.selected_tower_type = None

    def get_tower_count(self):
        """ Returns the number of towers placed. (testing purpose) """
        return len(self.towers)

    def get_enemy_count(self):
        """ Returns the number of enemies currently in the game. (testing purpose) """
        if self.enemy_manager:
            return len(self.enemy_manager.enemies)
        return 0

    def get_projectile_count(self):
        """ Returns the number of active projectiles. (testing purpose) """
        return len(self.projectiles)
