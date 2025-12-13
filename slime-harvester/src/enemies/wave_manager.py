""" This module will manage enemy waves and difficulty scaling. """
from settings import WAVE_CONFIG, ENEMY_CONFIG

class WaveManager:
    """ This class manages enemy waves and difficulty scaling. """
    def __init__(self, enemy_manager):
        self.wave_config = WAVE_CONFIG
        self.current_wave = 1
        self.remaining_enemies = self.wave_config[self.current_wave]["enemy_count"]
        self.enemy_manager = enemy_manager
        self.wave_cooldown = 0
        self.enemy_config = ENEMY_CONFIG

    def spawn_wave(self):
        """ Manages enemy spawn waves. """
        wave = self.wave_config[self.current_wave]
        self.wave_cooldown -= 1
        if self.remaining_enemies == 0:
            if self.is_wave_cooldown_active() is False:
                self.current_wave += 1
                self.remaining_enemies = self.wave_config[self.current_wave]["enemy_count"]
        else:
            if self.remaining_enemies == 1:
                self.reset_wave_cooldown()
            if self.enemy_manager.add_enemies(self.enemy_config[wave["enemy_type"]]) is True:
                self.remaining_enemies -= 1
                spawn_interval = self.wave_config[self.current_wave]["spawn_interval"]
                self.enemy_manager.update_interval(spawn_interval)

    def is_wave_cooldown_active(self):
        """ Returns True if wave cooldown is active. """
        if self.wave_cooldown <= 0:
            return False
        return True

    def reset_wave_cooldown(self):
        """ Resets wave cooldown. """
        self.wave_cooldown = 300
