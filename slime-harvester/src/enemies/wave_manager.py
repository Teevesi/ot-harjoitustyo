""" This module will manage enemy waves and difficulty scaling. """
from settings import WAVE_CONFIG

class WaveManager:
    """ This class manages enemy waves and difficulty scaling. """
    def __init__(self, enemy_manager):
        self.wave_config = WAVE_CONFIG
        self.current_wave = 1
        self.remaining_enemies = self.wave_config[self.current_wave]["enemy_count"]
        self.enemy_manager = enemy_manager

    def spawn_wave(self):
        """ Manages enemy spawn waves. """
        wave = self.wave_config[self.current_wave]
        if self.remaining_enemies == 0:
            self.current_wave += 1
            self.remaining_enemies = self.wave_config[self.current_wave]["enemy_count"]
        else:
            if self.enemy_manager.add_enemies(wave["enemy_image"]) is True:
                self.remaining_enemies -= 1
                spawn_interval = self.wave_config[self.current_wave]["spawn_interval"]
                self.enemy_manager.update_interval(spawn_interval)
                

        




        
        

