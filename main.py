from scenes import left_or_right as lr
from utils import errors as err, make_choices as mc


def main():
    print("Welcome to the trial of my python text-based adventure!\n")
    print("Onto the first room!\n\n")

    lr.left_or_right()
    lr.left_or_right_var()

    print("Thanks for playing!\n")
    print("That's all we've got for now, check back later for more!\n")


if __name__ == '__main__':
    main()
