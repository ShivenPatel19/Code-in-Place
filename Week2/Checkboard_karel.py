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
    
    while left_is_clear(): #karel to repeat these functions as long as left is clear when facing east, taking karel to the top
        odd_row() #fills row with beepers in odd columns and then returns to original position in first column of row facing east
        move_up_reset() #moves karel up one row and then faces east
        even_row() #fills row with beepers in even number columns and then returns karel to colun 1 facing east
        if left_is_clear(): #has karel move up and reset only if there is space to do so 
            move_up_reset()
    check_below() #checks to see if there is a beeper one space south of current position (TRUE indicating and odd row below) and has karel place an even row if so, otherwise returns karel to top left corner 
    turn_right()
    move_to_wall()
    turn_left()


def odd_row():
    if front_is_clear():
        while front_is_clear():
            put_beeper()
            move()
            if front_is_clear():
                move()
        check_for_back() #checks for a beeper behind karel, if TRUE karel will return to the position without placing a beeper, if FALSE karel will return to original position and place a beeper to fix fencepost problem
        come_back()
    else:
        put_beeper()

def check_for_back():
    step_back()
    if beepers_present():
        move()
    else:
        move()
        put_beeper()

def check_below():
    turn_right()
    move()
    if no_beepers_present():
        step_back()
        turn_left()
        odd_row()
    else:
        step_back()
        turn_left()
def come_back():
    turn_around()
    move_to_wall()
    turn_around()

def move_up_reset():
    turn_left()
    move()
    turn_right()

def even_row():
    if front_is_clear():
        while front_is_clear():
            if front_is_clear():
                move()
            put_beeper()
            if front_is_clear():
                move()
        come_back()

def move_to_wall():
    while front_is_clear():
        move()

def turn_right():
    for i in range(3):
        turn_left()

def step_back():
    turn_around()
    move()
    turn_around()
            

def turn_around():
    for i in range(2):
        turn_left()                

#because here there is a wall in front, Karel cannot 
#keep filling, he needs to go to the next line
#in position to fill
 

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
