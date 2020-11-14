class MyCharacter:
    def __init__(self):
        self.name = ""
        self.inventory = []

    def set_name(self):
        self.name = input("What is your name?\n")

    def add_inventory(self, new_obj):
        self.inventory.append(new_obj)

    def remove_inventory(self, obj):
        self.inventory.remove(obj)

    def view_inventory(self):
        string = "Your inventory consists of:\n"
        for item in self.inventory:
            string.__add__(str(item.get("name"), "\t"))
