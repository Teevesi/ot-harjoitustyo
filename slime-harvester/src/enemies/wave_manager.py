""" This module will manage enemy waves and difficulty scaling. """
from settings import WAVE_CONFIG

class WaveManager:
    """ This class manages enemy waves and difficulty scaling. """
    def __init__(self):
        self.wave_config = WAVE_CONFIG
        self.current_wave = 0
