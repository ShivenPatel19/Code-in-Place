from karel.stanfordkarel import *

def move_next():
    put_beeper()
    move()
    put_beeper()
    turn_left()
    move()
    put_beeper()
    turn_left()
    turn_left()
    move()
    turn_left()

def main():
    move_next()
    move()
    move()
    move_next()
    move()
    move()
    move_next()
    move()
    move()
    move_next()


# don't edit these next two lines
# they tell python to run your main function
if __name__ == '__main__':
    main()