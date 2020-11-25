from enum import Enum, auto
from utils.named_list import NamedList


names = ["damage", "reach", "weight", "durability"]


class Type(Enum):
    KNIFE = auto()
    ARMING_SWORD = auto()
    BROADSWORD = auto()
    AXE = auto()
    GREATAXE = auto()


class Quality(Enum):
    RUSTY = auto()
    DAMAGED = auto()
    MEDIOCRE = auto()
    NICE = auto()
    MASTER = auto()


def getTypeValues(type):
    if type == Type.KNIFE:
        return {'name': "Knife",
                'values': [5, 1, 1, 120]
                }
    if type == Type.ARMING_SWORD:
        return {'name': "Arming Sword",
                'values': [6, 5, 2, 75]
                }
    if type == Type.BROADSWORD:
        return {'name': "Broadsword",
                'values': [8, 10, 4, 75]
                }
    if type == Type.AXE:
        return {'name': "Axe",
                'values': [7, 5, 4, 100]
                }
    if type == Type.GREATAXE:
        return {'name': "Greataxe",
                'values': [10, 10, 6, 100]
                }


def getQualityModifiers(quality):
    if quality == Quality.RUSTY:
        return {'name': "Rusty ",
                'values': [-2, 0, 0, 0.75],
                'mod_type': ["+", "+", "+", "*"]
                }
    if quality == Quality.DAMAGED:
        return {'name': "Damaged ",
                'values': [-1, 0, 0, 0.85],
                'mod_type': ["+", "+", "+", "*"]
                }
    if quality == Quality.MEDIOCRE:
        return {'name': "Mediocre ",
                'values': [0, 0, 0, 1],
                'mod_type': ["+", "+", "+", "*"]
                }
    if quality == Quality.NICE:
        return {'name': "Nice ",
                'values': [1, 0, 0, 1.1],
                'mod_type': ["+", "+", "+", "*"]
                }
    if quality == Quality.MASTER:
        return {'name': "Master ",
                'values': [3, 0, 0, 1.5],
                'mod_type': ["+", "+", "+", "*"]
                }


def make_weapon(_type, _quality):
    type_ = getTypeValues(_type)
    quality = getQualityModifiers(_quality)
    name = quality['name'] + type_['name']
    values = type_['values']
    mods = quality['mod_type']
    val_change = quality['values']

    for i in range(len(values)):
        if mods[i] == "+":
            values[i] += val_change[i]
        elif mods[i] == "*":
            values[i] *= val_change[i]
        else:
            pass
    return NamedList(name, names, values)
