from PlayerInfo.player_character import Player


def wait():
    input("Press enter to continue...")
    print("...\n")


def character_creator(gamestate):
    print("Welcome to your adventure!\n")
    print("Before we begin, there a few housekeeping things we need to take care of\n\n")
    wait()

    name = input("Tell me, what is your name?\t")
    player = Player(name)

    print("Alright " + name + ", I think we're just about ready to begin!")
    wait()
    print("Ok then! Let's begin!")
