import utils.make_choices as mc
import utils.errors as err


def left_or_right():
    lr = input("You reach a fork in the road, do you turn left or right?\n")

    def loop(direc=lr):
        direction = ""
        try:
            direction = mc.binary_option_novar(direc, "left", "right")
        except err.NoSuchOption:
            direc = input("Please enter \"left\" or \"right\"\n")
            direction = loop(direc)
        finally:
            return direction

    lr = loop()
    if lr == "left":
        go_left()
    else:
        go_right()


def left_or_right_var():
    lr = input("You reach a fork in the road, do you turn left or right?\n")

    def loop(direc=lr):
        direction = ""
        try:
            direction = mc.binary_option_var(direc, "left", "right")
        except err.NoSuchOption:
            direc = input("Please enter \"left\" or \"right\"\n")
            direction = loop(direc)
        finally:
            return direction

    lr = loop()
    if lr == "left":
        go_left()
    else:
        go_right()


def go_left():
    print("You went left\n")


def go_right():
    print("You went right\n")
