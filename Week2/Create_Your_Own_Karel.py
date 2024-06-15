from karel.stanfordkarel import *

def main():
    for i in range(4):
        move()
    two_beepers()  
    turn_left()
    move()
    put_beeper()
    turn_right()
    move()
    turn_left()
    move()
    two_beepers()
    turn_left()
    move()
    put_beeper()
    move()
    turn_left()
    move()
    turn_right()
    two_beepers()
    turn_right()
    move()
    put_beeper()
    turn_left()
    move()
    turn_left()
    move()
    two_beepers()
    turn_left()
    move()
    put_beeper()
    turn_right()
    move()
    turn_left()



def turn_right():
    turn_left()    
    turn_left()    
    turn_left()    
      
def two_beepers():
    for i in range(2):
        put_beeper()
        move()  


# don't change this code
if __name__ == '__main__':
    main()
