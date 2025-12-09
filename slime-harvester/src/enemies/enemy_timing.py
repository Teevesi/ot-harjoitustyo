from enemies.enemy_movement import Enemy


class Timer():
    def __init__(self):
        self.timer = 0

    def update(self):
        self.timer += 1

    def get_timer(self):
        return self.timer//60

    def get_real_timer(self):
        return self.timer

class EnemyTiming:
    def __init__(self):
        self.spawn_interval = 60
        self.last_spawn_time = 0
        self.min_interval = 2

    def get_interval(self, current_time):
        interval = self.spawn_interval - (current_time // 100)
        return max(self.min_interval, interval)

    def can_spawn(self, current_time):
        interval = self.get_interval(current_time)
        if current_time - self.last_spawn_time >= interval:
            self.last_spawn_time = current_time
            return True
        return False

    def reset(self):
        self.last_spawn_time = 0

    def spawn_enemy(self, enemy_path, enemy_speed):
        return Enemy(enemy_path.path, enemy_speed)
