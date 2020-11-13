from utils.errors import NoSuchOption


def binary_option_novar(inputstr, choice1, choice2):
    if inputstr.lower() == choice1.lower():
        return choice1
    elif inputstr.lower() == choice2.lower():
        return choice2
    else:
        raise NoSuchOption


def binary_option_var(inputstr, choice1, choice2):
    try:
        return binary_option_novar(inputstr, choice1, choice2)
    except NoSuchOption:
        pass

    if inputstr.lower().find(choice1.lower()) > 0 > inputstr.lower().find(choice2.lower()):
        return choice1
    elif inputstr.lower().find(choice1.lower()) < 0 < inputstr.lower().find(choice2.lower()):
        return choice2
    elif inputstr.lower().find(choice1.lower()) > 0 < inputstr.lower().find(choice2.lower()):
        raise NoSuchOption
    elif choice1[0].lower() != choice2[0].lower() and len(inputstr) == 1:

        if inputstr[0].lower() == choice1[0].lower():
            return choice1
        elif inputstr[0].lower() == choice2[0].lower():
            return choice2

    else:
        raise NoSuchOption


def list_option_novar(inputstr, choices):
    for choice in choices:
        if inputstr.lower() == choice.lower():
            return choice

    raise NoSuchOption


def list_option_var(inputstr, choices, aliases=None, use_first_letter=True):
    try:
        return list_option_novar(inputstr, choices)
    except NoSuchOption:
        pass

    selection = None
    for choice in choices:
        if inputstr.lower().find(choice.lower()) > 0:
            if selection is not None:
                selection = choice
            else:
                selection = None
                break

    if selection is not None:
        return selection

    if aliases is not None and len(choices) == len(aliases):
        try:
            return list_option_novar(inputstr, aliases)
        except NoSuchOption:
            pass

        for choice in aliases:
            if inputstr.lower().find(choice.lower()) > 0:
                if selection is not None:
                    selection = choice
                else:
                    selection = None
                    break

        if selection is not None:
            return selection

    if use_first_letter:
        for choice in choices:
            if inputstr.lower()[0] == choice.lower()[0]:
                if selection is not None:
                    selection = choice
                else:
                    raise NoSuchOption

        if selection is not None:
            return selection

    raise NoSuchOption
