from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    first_round()
    find_center()
    """
    odd: in the middle, but facing west
    even: on the right of middle, facing east
    """
    correct()  #correct odd and even 

#put beeper to find the center
def first_round():
    move()
    while front_is_clear():
        if no_beepers_present():
            move()
    turn_around()
    put_beeper()
    move()
    while front_is_clear():
        move()
    turn_around()
    move()

def find_center():
    if no_beepers_present():
        put_beeper()
        go_next_beeper()


def correct():
    if right_is_blocked():
        turn_around()
        pick_beeper()
        move()
        put_beeper()
        turn_around()
    to_east()

def go_next_beeper():
    move()
    while no_beepers_present():
        move()
    if beepers_present():
        turn_around()
        pick_beeper()
        move()
        find_center()


def go_to_wall():
    while front_is_clear():
        move()
    turn_around()

#direction helper function
def turn_right():
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

def to_south():
    while not_facing_south():
        turn_left()

def to_east():
    while not_facing_east():
        turn_left()

if __name__ == '__main__':
    main()