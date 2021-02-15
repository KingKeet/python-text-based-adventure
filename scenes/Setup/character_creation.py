from PlayerInfo.player_character import Player
from PlayerInfo.race_database import Race, print_races


def wait():
    input("Press enter to continue...")
    print("...\n")


def character_creator(gamestate):
    print("Welcome to your adventure!\n")
    print("Before we begin, there a few housekeeping things we need to take care of\n\n")
    wait()

    name = input("Tell me, what is your name?\t")
    print("I see I see... so... ")
    race = None

    while True:
        print("who are your people?\n\nPlease select one of the following:\n")
        print_races()
        race = int(input())
        for r in Race:
            if race == r.value:
                race = r
                break

        if not isinstance(race, Race):
            print("I'm sorry, I didn't catch that... ")
            continue
        else:
            break

    player = Player(name, race)
    gamestate.update('player', player)

    print(f"Alright {name} the {race.name}, I think we're just about ready to begin!")
    wait()
    print("Ok then! Let's begin!")
