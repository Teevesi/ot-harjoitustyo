
class HealthBar():
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def current_health(self):
        return self.health
