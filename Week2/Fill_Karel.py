from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    while left_is_clear():
        fill_row()
        reset_to_next_row()
    fill_row()

"""
I want Karel to put beepers until the wall
I want Karel to turn around
I want Karel to go to the next level
Repeat until top final one last time
"""

def fill_row():
    #Fills row with beepers
    #Pre: Karel is facing right at start of row
    #Post: Karel is at end of row, beepers placed, facing right
    while front_is_clear():
        fill_corner()
        move()
    fill_corner()

def fill_corner():
    
    #Fills corner with beeper
    #Pre: the corner Karel is on has no beepers
    #Post: the corner Karel is on has a beeper
    
    if no_beepers_present():
        put_beeper()


def reset_to_next_row():
    #Pre: Karel is at end of row, facing right
    #POst: Karel is at beginning of next row, facing right
    turn_around()
    move_to_wall()
    turn_right()
    move()
    turn_right()


def turn_around():
    turn_left()
    turn_left()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()