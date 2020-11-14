from enum import Enum, auto
from utils.named_list import NamedList


class Info:
    _type = None
    _id = None
    stats = ()


class ItemTypes(Enum):
    WEAPON = auto()
    ARMOR = auto()
    FOOD = auto()


class Weapons:
    names = ["damage", "reach", "weight", "durability"]

    RUSTY_KNIFE = NamedList(names, [3, 1, 1, 120])
    RUSTY_SHORTSWORD = NamedList(names, [4, 5, 2, 75])
    RUSTY_BROADSWORD = NamedList(names, [6, 10, 4, 75])
    RUSTY_AXE = NamedList(names, [5, 5, 4, 100])
    RUSTY_GREATAXE = NamedList(names, [8, 10, 6, 100])
