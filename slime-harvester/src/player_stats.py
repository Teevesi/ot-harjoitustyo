
class HealthBar():
    """ Class to manage player's health. """
    def __init__(self, max_health):
        self.max_health = max_health
        self.health = max_health

    def take_damage(self, amount):
        """ Decrease health by the specified amount. """
        self.health = max(0, self.health - amount)

    def current_health(self):
        """ Returns the current health value. """
        return self.health

class Currency():
    """ Class to manage player's currency. """
    def __init__(self, starting_amount):
        self.amount = starting_amount

    def increase(self, amount):
        """ Increase the currency by the specified amount. """
        self.amount += amount

    def decrease(self, amount):
        """ Decrease the currency by the specified amount if sufficient funds exist. """
        if amount > self.amount:
            return False
        self.amount -= amount
        return True

    def current_amount(self):
        """ Returns the current currency amount. """
        return self.amount
