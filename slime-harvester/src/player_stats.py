from settings import max_health



class HealthBar():
    def __init__(self, max_health):
        self.max_health = max_health
        self.current_health = max_health

    def take_damage(self, amount):
        self.current_health = max(0, self.current_health - amount)

    def is_alive(self):
        return self.current_health > 0
    