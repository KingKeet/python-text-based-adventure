from utils.errors import NoSuchOption


def binary_option_novar(inputstr, choice1, choice2):
    if inputstr.lower() == choice1.lower():
        return choice1
    elif inputstr.lower() == choice2.lower():
        return choice2
    else:
        raise NoSuchOption
