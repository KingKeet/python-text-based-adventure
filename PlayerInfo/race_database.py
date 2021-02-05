from enum import Enum, auto


class Race(Enum):
    Human = auto()
    Elf = auto()
    Dwarf = auto()
    Halfling = auto()


def print_races():
    i = 1
    for race in Race:
        print(f"\n[{i}]\t{race}")
        i = i + 1
