from utils import make_choices as mc, errors as err


def three_doors():
    print("You come into a room with three doors.\n")
    door = input("Do you enter door one, two, or three?\n")

    def loop(dr=door):
        ans = None
        try:
            ans = mc.list_option_novar(dr, ["one", "two", "three"])
        except err.NoSuchOption:
            dr = input("please say \"one\", \"two\", or \"three\"\n")
            ans = loop(dr)
        finally:
            return ans

    door = loop()
    if door == "one":
        door_one()
    elif door == "two":
        door_two()
    else:
        door_three()


def three_doors_var():
    print("You come into a room with three doors.\n")
    door = input("Do you enter door one, two, or three?\n")

    def loop(dr=door):
        ans = None
        try:
            ans = mc.list_option_var(dr, ["one", "two", "three"], aliases=["1", "2", "3"], use_first_letter=False)
        except err.NoSuchOption:
            dr = input("please say \"one\", \"two\", or \"three\"\n")
            ans = loop(dr)
        finally:
            return ans

    door = loop()
    if door == "one" or door == "1":
        door_one()
    elif door == "two" or door == "2":
        door_two()
    else:
        door_three()


def door_one():
    print("You went through the first door")


def door_two():
    print("You went through the second door")


def door_three():
    print("You went through the third door")
