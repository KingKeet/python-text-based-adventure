from PlayerInfo.inventory import Inventory
from PlayerInfo.race_database import Race


class Player:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.inventory = Inventory()

    def get_name(self):
        return self.name
