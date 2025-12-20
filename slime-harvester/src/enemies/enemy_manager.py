from enemies.enemy_timing import EnemyTiming
from settings import ENEMY_CONFIG

class EnemyManager:
    """ This class manages all enemies in the game. """
    def __init__(self, timer, enemy_path, hp_bar):
        self.enemies = []
        self.enemy_timing = EnemyTiming()
        self.enemy_path = enemy_path
        self.timer = timer
        self.hp_bar = hp_bar
        self.enemy_config = ENEMY_CONFIG

    def add_enemies(self, enemy_type_dict=None):
        """Attempt to spawn an enemy.
        Returns True if an enemy was spawned, False otherwise.
        """
        if self.enemy_timing.can_spawn(self.timer.get_real_timer()) is True:
            if enemy_type_dict is None:
                enemy_type_dict = self.enemy_config["red_slime"]
            new_enemy = self.enemy_timing.spawn_enemy(self.enemy_path, enemy_type_dict)
            self.enemies.append(new_enemy)
            return True
        return False

    def update_enemies(self):
        """Update all enemies."""
        for enemy in list(self.enemies):  # Use list() to avoid modification during iteration
            if enemy.update() is True:
                self.enemies.remove(enemy)
                self.hp_bar.take_damage(1)

    def update_interval(self, new_interval):
        """Update spawn interval via EnemyTiming."""
        self.enemy_timing.update_interval(new_interval)

    def remove(self, enemy):
        """Remove the specified enemy from the list."""
        if enemy in self.enemies:
            self.enemies.remove(enemy)

    def get_enemy_hit_action(self, enemy):
        if enemy.enemy_type["next_type"] == 0:
            self.remove(enemy)
        else:
            enemy.swap_enemy_type(self.enemy_config[enemy.enemy_type["next_type"]])
