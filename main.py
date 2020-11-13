from scenes.ExampleScenes import three_doors as doors, left_or_right as lr


def main():
    print("Welcome to the trial of my python text-based adventure!\n")
    print("Onto the first room!\n\n")

    lr.left_or_right()
    lr.left_or_right_var()
    doors.three_doors()
    doors.three_doors_var()

    print("Thanks for playing!\n")
    print("That's all we've got for now, check back later for more!\n")


if __name__ == '__main__':
    main()
