
class HealthBar():
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def current_health(self):
        return self.health

class Currency():
    def __init__(self, starting_amount):
        self.amount = starting_amount

    def increase(self, amount):
        self.amount += amount

    def decrease(self, amount):
        if amount > self.amount:
            return False
        self.amount -= amount
        return True

    def current_amount(self):
        return self.amount
