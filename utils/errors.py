class NoSuchOption(Exception):
    default_txt = "ERROR: No such option is available.\n"

    def __init__(self, message=default_txt):
        self.message = message


class InventoryFullException(Exception):
    default_txt = "Inventory is full!\n"

    def __init__(self, message=default_txt):
        self.message = message
