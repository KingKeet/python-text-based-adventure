from scenes.ExampleScenes import three_doors as doors, left_or_right as lr
from scenes.Setup import character_creation as cc
from PlayerInfo.player_character import Player
from Gamestate import gamestate as gs, room_data as rm


def examples():
    print("Welcome to the trial of my python text-based adventure!\n")
    print("Onto the first room!\n\n")

    lr.left_or_right()
    lr.left_or_right_var()
    doors.three_doors()
    doors.three_doors_var()

    print("Thanks for playing!\n")
    print("That's all we've got for now, check back later for more!\n")


def main():
    state = gs.Gamestate()

    print("Welcome to the trial of my python text-based adventure!\n\n")
    cc.character_creator(state)


if __name__ == '__main__':
    main()
