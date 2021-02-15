from scenes import *
from scenes.Setup import character_creation as cc


class TextBox:
    def __init__(self):
        self.contents = ""

    def get_contents(self):
        return self.contents

    def update(self, txt):
        self.contents = txt
