from enemy_movement import Enemy



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

    def can_spawn(self, current_time):
        if current_time - self.last_spawn_time >= self.spawn_interval:
            self.last_spawn_time = current_time
            return True
        return False
    
    def reset(self):
        self.last_spawn_time = 0

    def spawn_enemy(self, enemy_path, enemy_speed):
        return Enemy(enemy_path.path, enemy_speed)