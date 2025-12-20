""" This module will manage enemy waves and difficulty scaling. """
from settings import WAVE_CONFIG, ENEMY_CONFIG
from generate_wave_config import endless_wave

class WaveManager:
    """ This class manages enemy waves and difficulty scaling. """
    def __init__(self, enemy_manager):
        self.wave_config = WAVE_CONFIG
        self.current_wave = 1
        self.remaining_enemies = self._get_current_wave_cfg()["enemy_count"]
        self.enemy_manager = enemy_manager
        self.wave_cooldown = 0
        self.enemy_config = ENEMY_CONFIG

    def spawn_wave(self):
        """Manage enemy spawn waves in coordination with EnemyManager timing. """
        cfg = self._get_current_wave_cfg()
        self.wave_cooldown -= 1

        if self.remaining_enemies == 0:
            if not self.is_wave_cooldown_active():
                self.current_wave += 1
                cfg = self._get_current_wave_cfg()
                self.remaining_enemies = cfg["enemy_count"]
            return

        if self.remaining_enemies == 1:
            self.reset_wave_cooldown()

        enemy_type_dict = ENEMY_CONFIG[cfg["enemy_type"]]
        if self.enemy_manager.add_enemies(enemy_type_dict) is True:
            self.remaining_enemies -= 1
            self.enemy_manager.update_interval(cfg["spawn_interval"])

    def is_wave_cooldown_active(self):
        """ Returns True if wave cooldown is active. """
        if self.wave_cooldown <= 0:
            return False
        return True

    def reset_wave_cooldown(self):
        """ Resets wave cooldown. """
        self.wave_cooldown = 180

    def _get_current_wave_cfg(self):
        """Return config dict for current wave. """
        if self.current_wave in self.wave_config:
            return self.wave_config[self.current_wave]
        return endless_wave(self.current_wave)
