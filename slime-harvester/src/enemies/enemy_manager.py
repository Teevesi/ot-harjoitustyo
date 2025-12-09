from enemies.enemy_timing import EnemyTiming
from settings import ENEMY_SPEED

class EnemyManager:
    def __init__(self, timer, enemy_path, hp_bar):
        self.enemies = []
        self.enemy_timing = EnemyTiming()
        self.enemy_path = enemy_path
        self.timer = timer
        self.hp_bar = hp_bar

    def add_enemies(self):
        if self.enemy_timing.can_spawn(self.timer.get_real_timer()) is True:
            new_enemy = self.enemy_timing.spawn_enemy(self.enemy_path, ENEMY_SPEED)
            self.enemies.append(new_enemy)

    def update_enemies(self):
        """Update all enemies (logic only, no rendering)."""
        for enemy in list(self.enemies):  # Use list() to avoid modification during iteration
            if enemy.update() is True:
                self.enemies.remove(enemy)
                self.hp_bar.take_damage(1)

    def remove(self, enemy):
        if enemy in self.enemies:
            self.enemies.remove(enemy)