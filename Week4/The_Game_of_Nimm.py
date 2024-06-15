def main():
    """
    Main function to run the game of Nimm.
    """
    print("The Ancient Game of Nimm\n")
    
    stones = 20
    player = 1

    while stones > 0:
        print(f"There are {stones} stones left.\n")
        remove = int(input(f"Player {player} would you like to remove 1 or 2 stones?  "))
        while remove not in [1, 2]:
            remove = int(input("\nPlease enter 1 or 2:  "))
        stones -= remove
        print()  # Empty print to create a new line after player input
        if stones == 0:
            print(f"Player {2 if player == 1 else 1} wins!\n")
            return
        player = 2 if player == 1 else 1

if __name__ == '__main__':
    main()


def main():
    print("hello world")

    # You can print variables
    x = 12
    print(x)

    # You can print many things
    print("Value of x", x)

if __name__ == "__main__":
    main()