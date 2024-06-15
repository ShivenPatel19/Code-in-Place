import random

def main():
    print("Delete this line and write your code here! :)")

if __name__ == '__main__':
    main()
    n = int(input("How many sides does your dice have? "))
    roll_result = random.randint(1, n)
    print("Your roll is", roll_result)


