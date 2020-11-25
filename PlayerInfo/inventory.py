from utils.errors import InventoryFullException, NoSuchOption


class Inventory:
    def __init__(self, max_weight=15):
        self.items = []
        self.current_weight = 0
        self.max_weight = max_weight

    def add_item(self, item, item_weight):
        if self.current_weight + item_weight < self.max_weight:
            self.items.append(item)
        else:
            raise InventoryFullException

    def drop_item(self, item, item_weight):
        if item in self.items:
            self.items.remove(item)
        else:
            raise NoSuchOption

    def to_string(self):
        out = ""
        tally = 0

        for item in self.items:
            out += item.to_string()
            if tally > 3:
                out += "\n"
                tally = 0
            else:
                out += "\t\t"
                tally += 1

        return out
