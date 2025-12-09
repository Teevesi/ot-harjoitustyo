from enemies.enemy_movement import Enemy


class Timer():
    """ This class manages the game timer. """
    def __init__(self):
        self.timer = 0

    def update(self):
        """ Tick the timer up by one frame. """
        self.timer += 1

    def get_timer(self):
        """ Returns the timer in seconds. """
        return self.timer//60

    def get_real_timer(self):
        """ Returns the timer in frames. """
        return self.timer

class EnemyTiming:
    """ This class manages enemy spawn timing. """
    def __init__(self):
        self.spawn_interval = 60
        self.last_spawn_time = 0
        self.min_interval = 2

    def get_interval(self, current_time):
        """ Calculates the current spawn interval based on the elapsed time. """
        # Decrease spawn interval over time, but not below min_interval
        interval = self.spawn_interval - (current_time // 100)
        return max(self.min_interval, interval)

    def can_spawn(self, current_time):
        """ Determines if an enemy can spawn based on the current time and spawn interval. """
        interval = self.get_interval(current_time)
        if current_time - self.last_spawn_time >= interval:
            self.last_spawn_time = current_time
            return True
        return False

    def reset(self):
        """ Resets the spawn timer. """
        self.last_spawn_time = 0

    def spawn_enemy(self, enemy_path, enemy_speed):
        """ Spawns a new enemy at the start of the path. """
        return Enemy(enemy_path.path, enemy_speed)
